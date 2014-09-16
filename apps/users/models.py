import random
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.db import models

from django.dispatch import receiver

import time

from json_field import JSONField

from rest_framework.authtoken.models import Token

from apps.geolocation.models import  District,Country,Region,Division, Ethnicity



 ########## Constants ##############
from apps.users.constants import TIME_ZONE_CHOICES
from apps.wisys.constants import GENDERS, MALE, USER_ROLE
from apps.wisys.models import AbstractBase
from django.utils import timezone
APP_NAME = 'users'
import pytz
########## Helpers ##############

class Profile(AbstractBase):
     user = models.OneToOneField(User, unique=True, related_name='profile')
     #first_name = models.CharField(verbose_name="First Name", max_length=30,null=True,blank=True)
     surname = models.CharField("User Surname",max_length=24)
     salutation = models.CharField(verbose_name="Salutation",max_length=12)
     birthdate = models.DateField("Birthday of User",null=True)
     sex = models.IntegerField(max_length=1,choices=GENDERS,default=MALE)
     address_1 = models.CharField(max_length=150,null=True)
     address_2 = models.CharField(max_length=150,blank=True)
     address_3 = models.CharField(max_length=150,blank=True)
     district = models.ForeignKey(District,related_name='profile_districts', null=True, default=None )
     country = models.ForeignKey(Country,related_name='profile_countries', null=True, default=None )
     division = models.ForeignKey(Division,related_name='profile_divisions', null=True, default=None )
     region = models.ForeignKey(Region,related_name='profile_regions', null=True, default=None )
     phone = models.CharField(max_length=15)
     mobile = models.CharField(max_length=15,null=True,blank=True)
     postcode = models.CharField(max_length=6,null=True)
     privacy = models.BooleanField(default=0)
     nickname = models.CharField(max_length=24,blank=True,null=True)


     def get_user_photo_file_name(self,filename):
         return 'images/user_photos/%s_%s' % (str(time.time()).replace('.','_'),filename )



     photo = models.ImageField(upload_to=get_user_photo_file_name,blank=True,null=True)
     extra = JSONField(default="{}",blank=True)

     def __unicode__(self):
         return "%s " % self.user.first_name


     def get_absolute_url(self):
         return reverse('users-detail', args=[self.id] )


     def get_photo(self):

         if self.photo:
            return self.photo
         else:
            if self.sex == MALE:
               return 'images/default/male_no_image_available.png'
            else:
               return 'images/default/female_no_image_available.jpg'


     @receiver(post_save, sender=User)
     def user_post_save_tasks(sender, instance, created, **kwargs):
         if created:
             profile, created = Profile.objects.get_or_create(user=instance)
             token, created = Token.objects.get_or_create(user=instance)
             


