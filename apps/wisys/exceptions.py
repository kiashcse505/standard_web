from django.http import HttpResponse
from rest_framework.exceptions import APIException


# from apps.wisys.helpers import give_404_response_with_error
#
#
# class WisysObjectNotFound(Exception):
#
#     def __init__(self,message,*args,**kwargs):
#         self.message = message
#         super(WisysObjectNotFound, self).__init__(*args, **kwargs)
#         self.render()
#
#     def render(self):
#         return HttpResponse(give_404_response_with_error(self.message))


class WisysRestFrameworkException(APIException):

    def __init__(self,detail,status_code,*args,**kwargs):
        self.detail = detail
        self.status_code = status_code
        super(WisysRestFrameworkException, self).__init__(*args, **kwargs)




    # def process_exception(self, request, exception):
    #     if type(exception) == Http:
    #         if not request.user.is_authenticated():
    #             return HttpResponseRedirect('/account/?next=' + request.path)