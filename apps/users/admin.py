from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin
from django.contrib.auth.models import User
from .models import Profile


class UserProfileInline(admin.TabularInline):
    model = Profile


class UserAdmin(DjangoUserAdmin):
    inlines = [ UserProfileInline,]

from import_export.admin import ImportExportModelAdmin


class UserAdmin(ImportExportModelAdmin):
    resource_class = Profile
    pass

admin.site.unregister(User)
admin.site.register(User, UserAdmin)