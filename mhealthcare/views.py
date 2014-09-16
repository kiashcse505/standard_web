from django.contrib.auth.models import User, Group
from django.shortcuts import render_to_response
from rest_framework import viewsets
from rest_framework import renderers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


from django.views.generic import ListView



#------------------------------------ WEB VIEWS ------------------------------------#


def home(self,*args, **kwargs):
    return render_to_response('base.html',{})

def login(self,*args, **kwargs):
    return render_to_response('mhealthcare/login.html',{})


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'patientList': reverse('patients-list', request=request, format=format),

        'questionList': reverse('question-list', request=request, format=format),

    })


# from django.views.generic import ListView, DetailView
# from django.contrib.auth import get_user_model
#
#
# class UserProfileDetailView(DetailView):
#     model = get_user_model()
#     slug_field = "username"
#     template_name = "user_detail.html"
#
#     def get_object(self, queryset=None):
#         user = super(UserProfileDetailView, self).get_object(queryset)
#         UserProfile.objects.get_or_create(user=user)
#         return user