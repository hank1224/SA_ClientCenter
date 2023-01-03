from rest_framework import viewsets
from rest_framework.permissions import AllowAny ,TokenAuthentication
from DBmanageApp.models import UserData
from RESTapiApp.serializers import Wash_UserSerializer, Carbon_UserSerializer

# Create your views here.
class Wash_UserViewSet(viewsets.ModelViewSet):
  queryset = UserData.objects.all()
  serializer_class = Wash_UserSerializer
  permission_classes = (AllowAny,)
  #Allowall 所有用戶、IsAuthenticated通過認證的用戶

# class Wash_UserViewSet(viewsets.ModelViewSet):
#   queryset = UserData.objects.all()
#   serializer_class = Wash_UserSerializer
#   permission_classes = (IsAuthenticated,)
#   authentication_classes = (TokenAuthentication,)

# import requests

# url = 'http://example.com/api/wash_user'
# headers = {'Authorization': 'Token 12345'}
# response = requests.get(url, headers=headers)


class Carbon_UserViewSet(viewsets.ModelViewSet):
  queryset = UserData.objects.all()
  serializer_class = Carbon_UserSerializer
  permission_classes = (AllowAny,)
  #Allowall 所有用戶、IsAuthenticated通過認證的用戶
