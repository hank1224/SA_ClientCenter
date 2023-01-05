from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import bad_request

from RESTapiApp.models import LineAPI_record
from RESTapiApp.serializers import *

from django.contrib.auth.models import User, Group





class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



# class Line_1ViewSet(viewsets.ModelViewSet):
#     queryset = LineAPI_record.objects.all()
#     serializer_class = Line_1Serializer
#     permission_classes = (AllowAny,)
#     http_method_names = ['get','post'] 
#     authentication_classes = [TokenAuthentication]

#     def create(self, request, *args, **kwargs):
#         serializer = Line_getRbackurlSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         create_indb = serializer.save()
#         Rserializer = Line_sendStateSerializer(instance=create_indb) #從資料庫出來不需要is_vaild，會報錯！
#         return Response(Rserializer.data)



