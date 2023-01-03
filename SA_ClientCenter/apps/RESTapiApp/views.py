from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from RESTapiApp.serializers import UserSerializer, GroupSerializer


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