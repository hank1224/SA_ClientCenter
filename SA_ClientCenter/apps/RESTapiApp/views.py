from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from RESTapiApp.models import LineAPI_record

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from RESTapiApp.serializers import UserSerializer, GroupSerializer
from RESTapiApp.serializers import Line_getBackurlSerializer , Line_getStateSerializer


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


class Line_getBackurlView(viewsets.ViewSet):
    def create_state(self, request):
    # 取得使用者提交的資料
      RbackURL = request.data
      # 使用序列化器處理資料
      serializer = Line_getBackurlSerializer(data=RbackURL)
      if serializer.is_valid():
        # 建立新資料
        new = serializer.save()
        new_State = new.Rstate
        print(new_State)








def make_token(request):
    from rest_framework.authtoken.models import Token
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    listA = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14']
    test=0
    for A in listA:
        user = User.objects.get(username=A)     
        Token.objects.create(user=user)
        test += 1
    HttpResponse("if 14, Success make token, test= " + str(test) )