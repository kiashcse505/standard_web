import urlparse
import user

from django.conf import settings
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, login, authenticate
    )
from django.contrib import messages
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.contrib.auth.forms import AuthenticationForm, SetPasswordForm
from django.contrib.auth.models import User,Permission,Group
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.models import get_current_site
from django.core.urlresolvers import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.utils.http import is_safe_url, base36_to_int, int_to_base36
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic.edit import FormView
from django.shortcuts import render_to_response,redirect, resolve_url,get_object_or_404
from datatableview import helpers
from apps.users.constants import THCC_SYSTEM_USER_ID
from apps.wisys import helpers as WisysHelpers

from apps.wisys.helpers import send_html_email
from apps.wisys.php import is_numeric
from .forms import  LoginCustom, UsernameRetrieveForm, PasswordResetRequestForm, MyUserCreationForm, MyUserUpdateForm,PasswordForm
from apps.users.forms import ProfileForm, MyUserCreationForm1
from django.template import RequestContext
from django.views.generic import ListView
from apps.geolocation.models import  District,Country
from mhealthcare.settings import HELPDESK_EMAIL
from .models import  Profile
from django.views.generic import TemplateView
from django.views.generic import CreateView,UpdateView,DetailView, DeleteView
from django.contrib.auth import  login as auth_login, get_user_model
#from eztables.views import DatatablesView
from django.http import HttpResponse
from django.utils import simplejson
from django.forms.models import model_to_dict
from apps.wisys.constants import GENDERS, ACTIVE, DELETED
from querystring_parser import parser
from apps.wisys.views import IrDatatableView





########################################## USERS #SUMMERY/ADD/EDIT/DELETE#   START ################################
class UserListView(IrDatatableView):
    template_name = 'users/user/users_home.html'
    #model = Profile
    queryset = Profile.objects.filter(user__is_active=True)
    datatable_options = {
        'structure_template': "wisys/datatable/default_table.html",
        'columns': [
            ('#','id', 'get_row_selection_box' ),
            'id',
            ('Username','username','get_username'),
            ('First Name', 'first_name', 'get_first_name'),
            'surname',
            ("Gender", 'sex', 'get_friendly_name' ),
            ('Address','address_1'),
            'district',
            'country',
            'postcode',
            'phone'
            # 'mobile',
            # 'credit_balance',
        ],
        'unsortable_columns': ['#','phone','postcode',],

    }
    extra_context = {
        "all_country": Country.objects.all(),
        "all_district": District.objects.all(),
    }

    def custom_search(self,queryset):
        for i in range(1,11):
            print i,self.request.GET[('sSearch_%d' % i)]
        kwargs = {}

        search_keys = ['id','surname__icontains',
            'address_1__icontains','country__name__icontains','district__name__icontains'
            ,'postcode']
        search_coloumn = [1,4,7,9,8,10]
        count=-1;
        for i in search_coloumn:
            count+=1;
            try:
                search_value = self.request.GET[('sSearch_%d' % i)]
            except Exception as ex:
                print ex
                continue

            if search_value:
                if i==1 or i==10:
                    kwargs[search_keys[count]] = int(search_value)
                else:
                    kwargs[search_keys[count]] = search_value

        qs = queryset.filter( **kwargs )
        print qs.query
        return qs

    def get_queryset(self):
        from django.contrib.auth.models import Group
        qs = super(IrDatatableView, self).get_queryset()
        current_user_group = self.request.user.groups.all()
        #print current_user_group[0]
        # print "This is Before query set"
        # print current_user_group[0].name


        if self.request.user.is_superuser:
            try:
                qs = self.custom_search(qs)
                qs = qs.filter(user__is_active=True)

                    #pass
            except Exception as ex:
                print ex
                pass
            return qs

    

        elif current_user_group[0].name == "Standard User":
            try:
                qs = self.custom_search(qs)
                qs = qs.filter(user__is_active=True).exclude(user__is_superuser=True)

                    #pass
            except Exception as ex:
                print ex
                pass
            return qs




    def get_first_name(self, instance , *args, **kwargs ):
        return WisysHelpers.link_to_model(instance, url=reverse_lazy('users-detail'))


    def get_is_active(self, instance , *args, **kwargs):
        return instance.user.is_active

    def get_username(self, obj , *args, **kwargs):
        return obj.user.username


class UserHomeView(UserListView):
    pass


class UserMixin(object):
    model = User
    context_object_name = "user"
    paginate_by = 10

    def get_success_url(self):
        return reverse('users-list')

    def get_queryset(self):
        return User.objects.all()


class ProfileMixin(object):
    model = Profile
    context_object_name = "profile"
    paginate_by = 10

    def get_success_url(self):
        return reverse('profile-list')

    def get_queryset(self):
        return Profile.objects.all()

from django.utils.decorators import method_decorator
from apps.users.decorator import group_required

class UserCreateView(UserMixin, CreateView):


    @method_decorator(group_required(["Admin User"]))
    def dispatch(self, *args, **kwargs):
        return super(UserCreateView, self).dispatch(*args, **kwargs)

    def get(self,request, *args, **kwargs):
        current_user_group = self.request.user.groups.all()
        if self.request.user.is_superuser :
         userForm = MyUserCreationForm()

        elif current_user_group[0].name == "Admin User":
            userForm = MyUserCreationForm()

        elif current_user_group[0].name == "Standard User":
            userForm = MyUserCreationForm1()

        profileForm = ProfileForm()
        return render_to_response('users/user/user_form.html', RequestContext(request, {
                'userForm': userForm,
                'profileForm': profileForm
            }))

    def post(self,request,*args,**kwargs):
        userForm = MyUserCreationForm(request.POST)
        profileForm = ProfileForm(request.POST, request.FILES)
        if userForm.is_valid() and profileForm.is_valid():
            specific_user = userForm.save()

            #print "u id >>>"
            #print specific_user.id



            userInstance = get_object_or_404(get_user_model(), id=specific_user.id)
            userForm2 = MyUserUpdateForm(request.POST or None, instance=userInstance )
            specific_user = userForm2.save()
            #specific_user.groups.add(Group.objects.get(name='THCC SYSTEM USERS'))

            print "user created ok"
            #USER_PROFILE_SYNC(request)


            profile_instance = get_object_or_404(Profile, id=specific_user.profile.id)
            profileForm = ProfileForm(request.POST, request.FILES,instance=profile_instance)
            specific_profile = profileForm.save(commit=False)
            #specific_profile.id = specific_user.id
            specific_profile.user = specific_user
            specific_profile.save()

            #print "u id >>>"
            #print specific_profile.id

            messages.add_message(request, messages.INFO, 'User %s created successfully' % ( specific_user.first_name ) )
            return redirect('user-home')

        return render_to_response('users/user/user_form.html', RequestContext(request, {
                                'userForm':userForm,
                                'profileForm':profileForm
                                }))


class FakeUserCreateView(UserMixin, CreateView):

    def get(self,request, *args, **kwargs):
        pass

    def post(self,request,*args,**kwargs):
        pass



class UserArchiveView(UserMixin, DeleteView):

    @method_decorator(group_required(["Admin User"]))
    def dispatch(self, *args, **kwargs):
        return super(UserArchiveView, self).dispatch(*args, **kwargs)

    def get(self, request, user_id, *args, **kwargs):
        profileInstance = get_object_or_404(Profile, id=user_id)
        user = get_object_or_404(User, pk=profileInstance.user.id)

        if user.is_superuser and request.user.is_superuser == False:
            return render(request,'users/authentication_message.html')

        user.is_active = False
        user.save()

        messages.add_message(self.request, messages.INFO, 'User Archived Successfully' )

        return HttpResponseRedirect( self.get_success_url() )


class UserUpdateView( UserMixin, UpdateView ):

    @method_decorator(group_required(["Admin User"]))
    def dispatch(self, *args, **kwargs):
        return super(UserUpdateView, self).dispatch(*args, **kwargs)

    def get(self,request,user_id, *args, **kwargs):

        aProfile = Profile.objects.get(id=user_id)
        aUser = User.objects.get(id=aProfile.user.id)


        if aUser.is_superuser and request.user.is_superuser == False:
            return render(request,'users/authentication_message.html')

        userForm = MyUserUpdateForm(instance=aUser)
        profileForm = ProfileForm(instance=aProfile)
        return render_to_response('users/user/user_form.html', RequestContext(request, {
                'userForm': userForm,
                'profileForm': profileForm
            }))

    def post(self, request, user_id,  *args, **kwargs ):

        profileInstance = get_object_or_404(Profile, id=user_id)
        userInstance = get_object_or_404(get_user_model(), id=profileInstance.user.id)

        if userInstance.is_superuser and request.user.is_superuser == False:
            return render(request,'users/authentication_message.html')

        userForm = MyUserUpdateForm(request.POST or None, instance=userInstance )
        profileForm = ProfileForm(request.POST or None, request.FILES or None, instance=profileInstance )
        if userForm.is_valid() and profileForm.is_valid():
            user = userForm.save()
            profile = profileForm.save()

            messages.add_message(request, messages.INFO, 'User %s updated successfully' % ( user.first_name ) )

            return redirect('user-home')


        return render_to_response('users/user/user_form.html',context_instance= RequestContext(request, {
                                   'userForm': userForm,
                                   'profileForm': profileForm
                                }))

from django.forms.fields import CheckboxInput

class UserDetailView(ProfileMixin, DetailView):
    template_name = 'users/user/user_detail.html'

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['form'] = MyUserUpdateForm
        return context






########################################## USERS #SUMMERY/ADD/EDIT/DELETE#   END ################################





########################################## LOGIN START ##############################################

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request, template_name='registration/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

        redirect_to = request.REQUEST.get(redirect_field_name, '')

        if request.user.is_authenticated():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                messages.add_message(request, messages.INFO, 'Welcome %s, %s.'  % (request.user.first_name, request.user.last_name) )
                return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)

        if request.method == "POST":
            form = authentication_form(request,data=request.POST)
            if form.is_valid():

                # Ensure the user-originating redirection url is safe.
                if not is_safe_url(url=redirect_to, host=request.get_host()):
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                # Okay, security check complete. Log the user in.
                auth_login(request, form.get_user())


                #print "login processsssssssss"

                if request.session.test_cookie_worked():
                    request.session.delete_test_cookie()

                messages.add_message(request, messages.INFO, 'Welcome %s, %s.'  % (request.user.first_name, request.user.last_name) )
                return HttpResponseRedirect(redirect_to)
            else:

                try:
                    email = form.cleaned_data['username']
                    password = form.cleaned_data['password']
                    emailer_user = User.objects.get(email=email)

                    if emailer_user and password:
                        user_cache = authenticate(username=emailer_user,password=password)
                        print "Printing emailer user cache"
                        print user_cache
                        if user_cache:

                            if not is_safe_url(url=redirect_to, host=request.get_host()):
                                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

                            #print "Printing emailer user cache"

                            # Okay, security check complete. Log the user in.
                            auth_login(request, user_cache)

                            #print "Printing emailer user cache"

                            #print "login processsssssssss"

                            if request.session.test_cookie_worked():
                                request.session.delete_test_cookie()

                            messages.add_message(request, messages.INFO, 'Welcome %s, %s.'  % (request.user.first_name, request.user.last_name) )
                            return HttpResponseRedirect(redirect_to)


                    #print "Printing emailer user"
                    #print emailer_user

                except Exception:
                    print "User NOt Found"
                    print Exception

        else:
            form = authentication_form(request)

        request.session.set_test_cookie()

        current_site = get_current_site(request)

        context = {
            'form': form,
            redirect_field_name: redirect_to,
            'site': current_site,
            'site_name': current_site.name,
        }
        if extra_context is not None:
            context.update(extra_context)
        return TemplateResponse(request, template_name, context,
                                current_app=current_app)




########################################## LOGIN END ##############################################






########################################## HCW START ##############################################
class WorkerListView(IrDatatableView):
    template_name = 'users/worker/workers_home.html'

    def get_queryset(self):
        return User.objects.filter(groups__name='Healthcare Worker')

    datatable_options = {
        'structure_template': "wisys/datatable/default_table.html",
        'columns': [
            ('#','id', 'get_row_selection_box' ),
            'id',
            'username',
            'first_name',
            'date_joined',
            'email',

        ],
        'unsortable_columns': ['#','phone','email',],

    }



class WorkerHomeView(WorkerListView):
    pass

class WorkerMixin(object):
    model = User
    context_object_name = "workers_list"
    paginate_by = 10

    def get_success_url(self):
        return reverse('workers-list')

    def get_queryset(self):
        return User.objects.filter(groups__name='Healthcare Worker')



@login_required
def listHealthworker(request):
     users = User.objects.filter(groups__name='Healthcare Worker')
     return render_to_response('users/list_healthworker.html',{'users':users} ,  context_instance=RequestContext(request)  )



########################################## HCW END ##############################################




########################################## Permission Start ##############################################
# 1 	Can add log entry                        19 	Can add site                               	31 	Can add access log
# 2 	Can change log entry                     20 	Can change site                             32 	Can change access log
# 3 	Can delete log entry                     21 	Can delete site                             33 	Can delete access log
# 7 	Can add group                            22 	Can add migration history                   34 	Can add settings  35 	Can Change settings
# 8 	Can change group                         23 	Can change migration history                36 	Can delete settings
# 9 	Can delete group                         24     Can delete migration history                79 	Can add module settings
# 13 	Can add content type                     25 	Can add key map                             80 	Can change module settings
#14 	Can change content type                  26 	Can change key map                          81 	Can delete module settings
#15 	Can delete content type                  27 	Can delete key map                          82 	Can add activity credits
#16 	Can add session                          28 	Can add access attempt                      83 	Can change activity credits
#17 	Can change session                       29 	Can change access attempt                   84 	Can delete activity credits
# 18 	Can delete session                       30 	Can delete access attempt
# from apps.users.decorator import group_required
# @group_required(["Super User"])



from apps.users.decorator import super_user_member_required
@login_required
@super_user_member_required
def listPermission(request):
    groups = Group.objects.all().prefetch_related('permissions').exclude(name="Patient")
    object_id_list = [1,2,3,7,8,9,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,169,170,171,61,62,63,73,74,75,76,77,78,79,80,81,82,83,84,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,104,105,109,110,111,115,116,117,118,119,120,151,152,153,154,155,156,157,158,159,160,161,162,163,164,165,166,167,168,169,170,171,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60]
    permissions = Permission.objects.exclude(id__in=object_id_list)

    if request.method == "GET" :

        permission_map = {}
        for aGroup in groups:
            permission_map[aGroup.id] = {}
            aGroupPermissoins = aGroup.permissions.all()
            #print "permission list:"
            #print  aGroupPermissoins
            for aPermissoin in aGroupPermissoins:
                permission_map[aGroup.id][aPermissoin.id] = True

        data = {
            'permissions' : permissions,
            'groups' : groups,
            'permission_map' : permission_map

        }
        return render_to_response('users/list_permission.html',data , context_instance=RequestContext(request))

    elif request.method == "POST":

        # groups = Group.objects.all().prefetch_related('permissions')
        # permissions = Permission.objects.filter(codename__like='mhealthcare%')
        post_dict = parser.parse(request.POST.urlencode('checks[]'))


        groups = Group.objects.all().prefetch_related('permissions').exclude(name="Patient")
        for aGroup in groups:
            aGroupPermissoins = aGroup.permissions.all()
            for aPermissoin in aGroupPermissoins:
                aGroup.permissions.remove(aPermissoin)


        permission_map = {}
        if 'perm_map' in post_dict:
            requested_perm_map = post_dict['perm_map']

            for permission_id in requested_perm_map:
                 permission_groups = requested_perm_map[permission_id]['']
                 if is_numeric(permission_groups):
                     permission_groups = [permission_groups]
                 Permission.objects.get(pk=permission_id).group_set.add(*permission_groups)


                 for aGroupId in permission_groups:
                    print "%s %s" % ( aGroupId, permission_id )
                    if aGroupId not in permission_map:
                        permission_map[ aGroupId ] = {}
                    permission_map[ aGroupId ][ permission_id ] = True
            messages.add_message(request, messages.INFO, 'Group Permissions Update successfully' )

        data = {
            'permissions' : permissions,
            'groups' : groups,
            'permission_map' : permission_map,
            'post' : post_dict
        }
        return render_to_response('users/list_permission.html',data , context_instance=RequestContext(request))


########################################## Permission End ##############################################




########################################## User Start ##############################################




class UsernameRetrieve(ListView):

    def get(self,request,*args,**kwargs):
        form = UsernameRetrieveForm()
        data = {'form': form }
        return render_to_response('username_retrieve/form.html', data,  context_instance=RequestContext(request))

    def post(self,request,*args,**kwargs):
        form = UsernameRetrieveForm(request.POST)

        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'from_email': settings.DEFAULT_FROM_EMAIL,
                'request': request,
            }

            form.send_retrieve_email(**opts)
            return HttpResponseRedirect(reverse('username-retrieve-done'))

        data = {'form': form }
        return render_to_response('username_retrieve/form.html', data,  context_instance=RequestContext(request))


class PasswordResetValidate(ListView):

    def get(self, request, *args, **kwargs):
        form = PasswordResetRequestForm()
        data = {'form': form }
        return render_to_response('password_reset/validate/form.html', data,  context_instance=RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = PasswordResetRequestForm(request.POST)
        if form.is_valid():
            opts = {
                'use_https': request.is_secure(),
                'from_email': settings.DEFAULT_FROM_EMAIL,
                'request': request,
            }
            form.send_reset_request_email(**opts)
            return HttpResponseRedirect(reverse('password-reset-validate-done'))

        data = {'form': form }
        return render_to_response('password_reset/validate/form.html', data,  context_instance=RequestContext(request))





# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
def password_reset_request(request, uidb36=None, token=None,domain_override=None,
                           request_email_subject_template='password_reset/request/email_subject.html',
                           request_email_template='password_reset/request/email.html',
                           request_email_done='password_reset/request/done.html',
                           token_generator=default_token_generator,
                           current_app=None, extra_context=None, use_https=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb36 is not None and token is not None  # checked by URLconf

    try:
        uid_int = base36_to_int(uidb36)
        user = UserModel._default_manager.get(pk=uid_int)
    except (ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True

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

        send_html_email( [HELPDESK_EMAIL], settings.DEFAULT_FROM_EMAIL , request_email_subject_template , request_email_template , context)

    else:
        validlink = False

    context = {
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, request_email_done, context,
                            current_app=current_app)



# Doesn't need csrf_protect since no-one can guess the URL
@sensitive_post_parameters()
@never_cache
def password_reset_process(request, uidb36=None, token=None,
                           domain_override = None,
                           template_name='password_reset/process/reset_form.html',
                           process_email_subject_template = 'password_reset/process/email_subject.html',
                           process_email_template = 'password_reset/process/email.html',
                           token_generator=default_token_generator,
                           set_password_form=SetPasswordForm,
                           post_reset_redirect=None,
                           use_https=False,
                           current_app=None, extra_context=None):
    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """
    UserModel = get_user_model()
    assert uidb36 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('django.contrib.auth.views.password_reset_complete')
    try:
        uid_int = base36_to_int(uidb36)
        user = UserModel._default_manager.get(pk=uid_int)
    except (ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        if request.method == 'POST':
            form = set_password_form(user, request.POST)
            if form.is_valid():
                form.save()

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
                    'password' : form.cleaned_data['new_password1'],
                    'protocol': use_https and 'https' or 'http',
                }

                send_html_email( [user.email], settings.DEFAULT_FROM_EMAIL, process_email_subject_template , process_email_template , context)
                return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(None)
    else:
        validlink = False
        form = None
    context = {
        'form': form,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)


########################################## User End ##############################################



class AdminUserPasswordChange(object):
    model = User
    context_object_name = "password"
    paginate_by = 10
    #slug_field = 'user_id'
    def get_success_url(self):
        return reverse('user-home')

    def get_queryset(self):
        return User.objects.all()

class PassWordChangeGlobal(AdminUserPasswordChange, UpdateView):
    template_name = 'users/user/password_change_form.html'
    form_class = PasswordForm
    pass








#this resolver script cleans all deleted patient and users from the system



def USER_PROFILE_SYNC(request):

     from django.db import connection
     cursor = connection.cursor()

     for aUser in User.objects.all():
         #aUser.profile.id = aUser.id
         #aUser.profile.save()
         #qr = "UPDATE `mhealthcarev2`.`users_profile` SET `id`='%s' WHERE `id`='%s';"

         parm = [aUser.id ,aUser.profile.id]

         cursor.execute("UPDATE `mhealthcarev2`.`users_profile` SET `id`='%s' WHERE `id`='%s';", parm)

     row = cursor.fetchone()

     return HttpResponse("Sync Done")




##this resolver adds pulse rate wherever blood_oxygen is listed
