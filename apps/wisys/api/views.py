# Create your views here.
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView


class IrBaseAPIView(APIView):
    authentication_classes = (TokenAuthentication , SessionAuthentication, )
    permission_classes = (IsAuthenticated,)

