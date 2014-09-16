# """
# This file demonstrates writing tests using the unittest module. These will pass
# when you run "manage.py test".

# Replace this with more appropriate tests for your application.
# """
# from django.contrib.auth.models import User

# from django.test import TestCase
# from apps.prms.models import Patient


# class SimpleTest(TestCase):
#     def test_basic_addition(self):
#         """
#         Tests that 1 + 1 always equals 2.
#         """
#         print "test running"
#         self.assertEqual(1 + 1, 2)


# # class FakeUserCreateTest(TestCase):
# #
# #     def test_createfakeuser(self):
# #         from django.contrib.auth.models import User
# #         from apps.users.models import Profile
# #         from django.http import HttpResponse
# #
# #         key_word = 'root'
# #
# #         for i in range(1,1000):
# #             try:
# #                 uname = ''.join([key_word,str((i+1))])
# #                 upassword = key_word
# #                 uemail = ''.join([key_word,str((i+1)),'@gmail.com'])
# #                 user = User.objects.create_user(uname, uemail, upassword)
# #                 print uemail
# #             except Exception as ex:
# #                 print 'User already created previously'
# #
# #                 #return HttpResponse('User already created previously')
# #         #return HttpResponse('User Created')

# from django.test import Client


# class UserTest(TestCase):
#     def setup(self):
#         self.client = Client()
#         session = self.client.session
#         session['siteid'] = 69
#         session.save()

#     def login(self,username,password):
#         response = self.client.get('/users/login/')
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/users/login/', {'username': username, 'password': password})
#         self.assertEqual(response.status_code, 302)

#     def logout(self):
#         response = self.client.get('/users/logout/')
#         self.assertEqual(response.status_code, 302)

#     def super_login(self):
#         response = self.client.get('/users/login/')
#         #print response.status_code
#         self.assertEqual(response.status_code, 200)
#         response = self.client.post('/users/login/', {'username': 'adminuser', 'password': 'admin123456'})
#         #print response.status_code
#         self.assertEqual(response.status_code, 302)

#         #print response.content
#     def super_logout(self):
#         response = self.client.get('/users/logout/')
#         self.assertEqual(response.status_code, 302)

#     def super_can_visit_exclusive_pages(self):
#         self.super_login()
#         response = self.client.get('/users/settings/')
#         #print response.status_code
#         self.assertEqual(response.status_code, 200)

#         response = self.client.get('/users/settings/list/')
#         #print response.status_code
#         self.assertEqual(response.status_code, 200)



#     def test_user(self):

# #user create test starts
#         self.super_login()
#         response = self.client.get('/users/create/')
#         #print response.status_code
#         self.assertEqual(response.status_code, 200)

#         user_create_data = {'username': 'monsur'
#                             ,'password1': '12','password2':'12'
#                             ,'salutation':'Mr.'
#                             ,'surname':'Bedi'
#                             ,'email':'kiashcse5051@gmail.com'
#                             ,'phone':"1212"
#                             ,'timezone':'1'
#                             ,'first_name':'Abdul'
#                             ,'last_name':'Hassan'
#                             ,'nickname':'bedi'
#                             ,'sex':'1'
#                             ,'mobile':'12122'
#                             ,'photo':''
#                             ,'user_role':'1'
#                             ,'groups':'2'
#                             ,'privacy':'0'
#                             }

#         response = self.client.post('/users/create/', user_create_data )
#         #print response.status_code
#         self.assertEqual(response.status_code, 302)


#         self.super_logout()

#         self.login("monsur","12")
#         self.logout()

# #user creation test is end
# #user update test starts

#         self.super_login()
#         aUser = User.objects.get(username="monsur")
#         #print aUser.id

#         response = self.client.get('/users/update/'+str(aUser.profile.id)+"/")
#         #print response.status_code
#         self.assertEqual(response.status_code, 200)

#         user_update_data = {'username': 'monsur'
#                             ,'password1': '12','password2':'12'
#                             ,'salutation':'Mrr.'
#                             ,'surname':'Bedis'
#                             ,'email':'kiashcsse5051@gmail.com'
#                             ,'phone':"12212"
#                             ,'timezone':'1'
#                             ,'first_name':'Abdul'
#                             ,'last_name':'Hassan'
#                             ,'nickname':'bedi3'
#                             ,'sex':'1'
#                             ,'mobile':'12122'
#                             ,'photo':''
#                             ,'user_role':'1'
#                             ,'groups':'2'
#                             ,'privacy':'0'
#                             }


#         response = self.client.post('/users/update/'+str(aUser.profile.id)+"/",user_update_data)
#         self.assertEqual(response.status_code, 302)

#         aUser = User.objects.get(username="monsur")

#         self.assertEqual(str(aUser.profile.nickname), "bedi3")

#         print "user updated ok"

#         self.super_logout()

# #user update test is done
# #patient create started
#         self.login("monsur","12")
#         response = self.client.get('/prms/patient/create/')
#         self.assertEqual(response.status_code, 200)

#         patient_create_data = {
#                              'salutation':'Mr.'
#                             ,'first_name':'Abdul'
#                             ,'surname':'Ahmed'
#                             ,'email':'kiashcsse5051@gmail.com'
#                             ,'phone':"12212"
#                             ,'last_name':'Hassan'
#                             ,'nickname':'bedi'
#                             ,'Dob_formate':'dd-mm-yy'
#                             ,'birthdate':'05-08-2014'
#                             ,'clinic_patient_ref':'abc'
#                             ,'address_1':'abc1'
#                             ,'address_2':'abc2'
#                             ,'address_3':'abc3'
#                             ,'country':'1'
#                             ,'division': '4'
#                             ,'district':'35'
#                             ,'region':'mosq'
#                             ,'postcode':'12354'
#                             ,'sex':'1'
#                             ,'mobile':'12122'
#                             ,'photo':''
#                             ,'ethnicity':'2'
#                             ,'religion':'6'
#                             ,'prefered_name':'Abdul'
#                             }

#         response = self.client.post('/prms/patient/create/',patient_create_data)
#         self.assertEqual(response.status_code, 302)

#         ap = Patient.objects.get(email='kiashcsse5051@gmail.com')
#         print ap.pin_code



#         self.logout()
# #patient create is done
# #user delete test is started

#         self.super_login()
#         response = self.client.get('/users/archive/'+str(aUser.profile.id)+"/")
#         self.assertEqual(response.status_code, 302)

#         print "user deleted ok"

# #user delete test is done





# """
# class FakeUserCreate(CreateView):

# ############  create fake 1000 users #####################


# def createfakeuser():
#     from django.contrib.auth.models import User
#     from apps.users.models import Profile
#     from django.http import HttpResponse

#     key_word = 'root'

#     for i in range(1,1000):
#         try:
#             uname = ''.join([key_word,str((i+1))])
#             upassword = key_word
#             uemail = ''.join([key_word,str((i+1)),'@gmail.com'])
#             user = User.objects.create_user(uname, uemail, upassword)
#             #print uemail
#         except Exception as ex:
#             print 'User already created previously'

#             return HttpResponse('User already created previously')
#     #return HttpResponse('User Created')


# """