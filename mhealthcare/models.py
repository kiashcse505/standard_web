from registration.models import User
from django.db import models

# class UserProfile(models.Model):
#     user = models.OneToOneField(User, unique=True)
#     bio = models.TextField(null=True)
#
#     def __unicode__(self):
#         return "%s's profile" % self.user
#
# def create_profile(sender, instance, created, **kwargs):
#     if created:
#         profile, created = UserProfile.objects.get_or_create(user=instance)
#
# # Signal while saving user
# from django.db.models.signals import post_save
# post_save.connect(create_profile, sender=User)