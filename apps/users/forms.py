#---------kiash-------------#
from __future__ import unicode_literals
import random
from django.contrib.auth.hashers import UNUSABLE_PASSWORD
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.db.models import Q
from django.forms import ModelForm
from django.template import loader
from django.utils.http import int_to_base36
import time
import pytz
from apps.wisys.helpers import validateEmail, send_plain_email_with_context, send_html_email
from mhealthcare import settings
from mhealthcare.settings import DATE_INPUT_FORMATS
from .models import  Profile
from django import forms
from django.contrib.auth.models import User,Group


from django.contrib.auth.forms import UserCreationForm,AuthenticationForm, UserChangeForm,SetPasswordForm,PasswordChangeForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import authenticate, get_user_model

from axes.models import AccessAttempt
#from django.contrib.auth.hashers import check_password, MAXIMUM_PASSWORD_LENGTH
from axes.models import AccessAttempt
from axes.decorators import  get_user_attempts
import axes
from django.db.models import Q


from axes.decorators import  get_user_attempts
from django.core.mail import send_mail
from apps.geolocation.models import Country,Division,District,Region


TIME_ZONE = (('1', 'UTC+05:30 (IST)',),('2', 'UTC+01:00 (CET)',),('3', 'UTC+02:00 (EET)',),('4', 'UTC+06:00',),('5', 'UTC+06:00 (BDT)',),('6', 'UTC (GMT)',),('7', 'UTC-02:00',),('8', 'UTC-03:00 (FKST)',),('9', 'UTC-03:00 (FKST)',),('10', 'UTC-04:00 (AST)',),('11', 'UTC-05:00',),('12', 'UTC-08:00',))


########################################## USER PROFILE RELATED  START  CLASS ################################

class ProfileForm(ModelForm):
    birthdate = forms.DateField( widget=forms.TextInput(attrs={'id':'datepicker',}), input_formats=DATE_INPUT_FORMATS,required=False )
    photo = forms.ImageField( label=('Photo'),required=False,error_messages ={'invalid':("Image files only")} )
    nickname = forms.CharField(max_length=30,widget=forms.TextInput,error_messages={'required':'This field id required'})
    country = forms.ModelChoiceField(widget = forms.Select(attrs = {'onchange' : "Dajaxice.apps.geolocation.updateDivision(Dajax.process, {'option': this.value})"}), queryset=Country.objects.all(), required=False)
    division = forms.ModelChoiceField(widget = forms.Select(attrs = {'onchange' : "Dajaxice.apps.geolocation.updateDistrict(Dajax.process, {'option': this.value})"}), queryset=Division.objects.all(), required=False)
    district = forms.ModelChoiceField(widget = forms.Select(attrs = {'onchange' : "Dajaxice.apps.geolocation.updateRegion(Dajax.process, {'option': this.value})"}), queryset=District.objects.all(), required=False)
    region = forms.ModelChoiceField(queryset=Region.objects.all(), required=False)
    postcode = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    mobile = forms.CharField(required=False)
    address_1 = forms.CharField(required=False)
    timezone =  forms.ChoiceField(widget=forms.Select, choices=TIME_ZONE)
    class Meta:
        model = Profile
        exclude = [ 'user','extra' ]


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput,required=True)
    last_name = forms.CharField(max_length=30,widget=forms.TextInput,required=False)
    email = forms.CharField(max_length=30,widget=forms.TextInput,error_messages={'required': 'This field is required.'})
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.exclude(name="Patient"),required=False)
    class Meta:
        model = get_user_model()
        fields = ( 'username','email','first_name','last_name','groups','is_superuser' )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email

class MyUserCreationForm1(UserCreationForm):

    first_name = forms.CharField(max_length=30,widget=forms.TextInput,required=True)
    last_name = forms.CharField(max_length=30,widget=forms.TextInput,required=False)
    email = forms.CharField(max_length=30,widget=forms.TextInput,error_messages={'required': 'This field is required.'})
    object_name_list =['Patient','Admin User']
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.exclude(name__in=object_name_list),required=False)
    class Meta:
        model = get_user_model()
        fields = ( 'username','email','first_name','last_name','groups','is_superuser' )

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email



class MyUserUpdateForm(UserChangeForm):
    first_name = forms.CharField(max_length=30,widget=forms.TextInput,required=True)
    last_name = forms.CharField(max_length=30,widget=forms.TextInput,required=False)
    email = forms.CharField(max_length=30,widget=forms.TextInput,error_messages={'required': 'This field is required'})
    groups = forms.ModelMultipleChoiceField(queryset=Group.objects.exclude(name="Patient"),required=False)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email

    class Meta:
        model = get_user_model()
        fields = ( 'username','email','first_name','last_name','groups','is_superuser' )

    def clean_password(self):
        return "" # This is a temporary fix for a django 1.4 bug


class PasswordForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ['password1','password2']
        exclude = ['username']
    def __init__(self, *args, **kwargs):
       super(UserCreationForm, self).__init__(*args, **kwargs)
       del self.fields['username']



class GroupForm(forms.Form):
    # name1 = Group.objects.all()
    # name = forms.ChoiceField(widget=forms.Select, choices=name1)
    # #name = [('', '-- choose a Group --'), ] + [(c.name, c.name) for c in Group.objects.all()]
    class Meta:
        model = Group
        fields = ['name',]

########################################## USER END   CLASS ################################








########################################## USER CUSTOM LOGIN CLASS  ################################


class LoginCustom(AuthenticationForm):

    error_messages = {
        'invalid_login': _("Username or password not recognised. %(attempts)s tries remaining."),
        'attempt_remaining' : _('%s tries remaining.'),
        'inactive': _("This account is inactive.")
    }

    def get_failure_remaining_count(self):
        failures = 0
        attempts = get_user_attempts(self.request)
        for attempt in attempts:
            failures = max(failures, attempt.failures_since_start)
        return settings.AXES_LOGIN_FAILURE_LIMIT - failures


    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')

        if username and password:
            self.user_cache = authenticate(username=username,
                                           password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'] % {
                        'attempts' : self.get_failure_remaining_count()
                    })
            elif not self.user_cache.is_active:
                #raise forms.ValidationError(self.error_messages['inactive'])
                raise forms.ValidationError(
                    self.error_messages['inactive'] % {
                        'attempts' : self.get_failure_remaining_count()
                    })
        self.check_for_test_cookie()
        return self.cleaned_data






########################################## USER END CLASS  ################################






########################################## USER USERNAME/PASSWORD RETRIEVE CLASS FORM   ################################


class UsernameRetrieveForm(forms.Form):

    error_messages = {
        'unknown': _("That email address isn't recognised. Please try again or contact support."),
        'unusable': _("The user account associated with this email "
                      "address cannot retrieve the username."),
    }
    email = forms.EmailField(label=_("Email"), max_length=254, required=True)

    def clean_email(self):
        """
        Validates that an active user exists with the given email address.
        """
        UserModel = get_user_model()
        email = self.cleaned_data["email"]
        self.users_cache = UserModel._default_manager.filter(email__iexact=email)
        if not len(self.users_cache):
            raise forms.ValidationError(self.error_messages['unknown'])
        if not any(user.is_active for user in self.users_cache):
            # none of the filtered users are active
            raise forms.ValidationError(self.error_messages['unknown'])

        return email


    def send_retrieve_email(self, domain_override=None,
             subject_template_name='username_retrieve/email_subject.html',
             email_template_name='username_retrieve/email.html',
             use_https=False,from_email=None, request=None):


        for user in self.users_cache:

            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override

            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'user': user,
                'protocol': use_https and 'https' or 'http',
            }

            send_html_email( [user.email], from_email, subject_template_name, email_template_name, context)



class PasswordResetRequestForm(forms.Form):

    error_messages = {
        'unknown': _("That email address isn't recognised. Please try again or contact support."),
        'unusable': _("The user account associated with this email "
                      "address cannot reset the password."),
    }
    email = forms.CharField(label=_("Email / Username"), max_length=254, required=True)

    def clean_email(self):
        """
        Validates that an active user exists with the given email address.
        """
        UserModel = get_user_model()
        email = self.cleaned_data["email"]

        if validateEmail( email ):
            self.users_cache = UserModel._default_manager.filter( Q(email__iexact=email) )
        else:
            self.users_cache = UserModel._default_manager.filter( Q(username__iexact=email) )

        if not len(self.users_cache):
            raise forms.ValidationError(self.error_messages['unknown'])
        if not any(user.is_active for user in self.users_cache):
            # none of the filtered users are active
            raise forms.ValidationError(self.error_messages['unknown'])
        if any((user.password == UNUSABLE_PASSWORD)
               for user in self.users_cache):
            raise forms.ValidationError(self.error_messages['unusable'])
        return email


    def send_reset_request_email(self, domain_override=None,
             subject_template_name='password_reset/validate/email_subject.html',
             email_template_name='password_reset/validate/email.html',
             use_https=False,token_generator=default_token_generator,
             from_email=None, request=None):


        for user in self.users_cache:

            if not domain_override:
                current_site = get_current_site(request)
                site_name = current_site.name
                domain = current_site.domain
            else:
                site_name = domain = domain_override

            context = {
                'email': user.email,
                'domain': domain,
                'site_name': site_name,
                'uid': int_to_base36(user.pk),
                'user': user,
                'token': token_generator.make_token(user),
                'protocol': use_https and 'https' or 'http',
            }

            send_html_email( [user.email], from_email, subject_template_name, email_template_name, context)


########################################## USER END CLASS  ################################






