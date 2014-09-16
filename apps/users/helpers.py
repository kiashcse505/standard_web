
from django.contrib import messages





# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import Permission, Group
#
#
# def add_custom_permission(app_label,model,permission_codename,permission_name,group_name):
#
#     contentType = ContentType.objects.get(app_label=app_label, model=model)
#     newPermission, created = Permission.objects.get_or_create(codename=permission_codename, name=permission_name, content_type=contentType)
#
#     group, created = Group.objects.get_or_create(name=group_name)
#     group.permissions.add(newPermission)


#
# # custom user related permissions
# def add_user_permissions(sender, **kwargs):
#     ct = ContentType.objects.get(app_label='auth', model='user')
#     addHCW, created = Permission.objects.get_or_create(codename='add_HCW', name='Add Healthcare Workers', content_type=ct)
#     addASU, created = Permission.objects.get_or_create(codename='add_ASU', name='Add iAppDragon SuperUser', content_type=ct)
#     addCAU, created = Permission.objects.get_or_create(codename='add_CAU', name='Add New HealthCare Center Admin User', content_type=ct)
#     addHCU, created = Permission.objects.get_or_create(codename='add_HCU', name='Add New Healthcare Center User', content_type=ct)
#     addCLAU, created = Permission.objects.get_or_create(codename='add_CLAU', name='Add New Clinic Admin User', content_type=ct)
#     addCLU, created = Permission.objects.get_or_create(codename='add_CLU', name='Add New Clinic User', content_type=ct)
#
#     mHealtSuper, created = Group.objects.get_or_create(name='MHealth Care SuperUser')
#     mHealtSuper.permissions.add(addHCW,addASU,addCAU,addHCU,addCLAU,addCLU)
#
#     appDragonSuper, created = Group.objects.get_or_create(name='iAppDragon SuperUser')
#     appDragonSuper.permissions.add(addHCW,addASU,addCAU,addHCU,addCLAU,addCLU)
#
#     healthCareWorker, created = Group.objects.get_or_create(name='Health Care Worker')
#
#     healthCareCenterAdmin, created = Group.objects.get_or_create(name='HealthCare Center Admin')
#     healthCareCenterAdmin.permissions.add(addHCW,addHCU)
#
#     healthCareCenterUser, created = Group.objects.get_or_create(name='HealthCare Center User')
#     healthCareCenterUser.permissions.add(addHCW)
#
#     clinicAdmin, created = Group.objects.get_or_create(name='Clinic Admin')
#     clinicAdmin.permissions.add(addCLU)
#
#     clinicUser, created = Group.objects.get_or_create(name='Clinic User')
#     clinicUser.permissions.add()
#


