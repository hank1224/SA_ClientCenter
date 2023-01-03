from django.contrib.auth.models import User, Group
from rest_framework import serializers
from DBmanageApp.models import UserData
from RESTapiApp.models import getLineURL, getPK_Line


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class getLineURL_Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = getLineURL
        fields = ('Rstate')

class Wash_UserSerializer(serializers.ModelSerializer):

  class Meta:
    model = UserData
    #fields = '__all__' 呼叫所有檔案
    #可以被傳送到智慧喜的資料
    fields = ['sUserID', 'sNickName', 'sPhone', 'sAddress', 'sPictureUrl']

    

class Carbon_UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserData
    #fields = '__all__' 呼叫所有檔案
    #可以被傳送到碳制郎的資料
    fields = ['sUserID', 'sName','sNickName', 'sPhone', 'sAddress', 'sEmail', 'sPictureUrl']