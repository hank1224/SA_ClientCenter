from django.contrib.auth.models import User, Group
from rest_framework import serializers
from DBmanageApp.models import UserData
from RESTapiApp.models import LineAPI_record
from uuid import uuid4

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class Line_getBackurlSerializer(serializers.Serializer):
    Rbackurl = serializers.CharField(max_length=200, required=True, label='用戶要求line後返回網址')

class Line_sendStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rstate', 'Rtime',]

class Line_getStateSerializer(serializers.Serializer):
    Rstate = serializers.CharField(max_length=36, required=True, label='從Line_1得到的Rstate')

class Line_sendUserIDSerializer(serializers.Serializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rstate', 'Rtime',]


class Carbon_UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserData
    #fields = '__all__' 呼叫所有檔案
    #可以被傳送到碳制郎的資料
    fields = ['sUserID', 'sName','sNickName', 'sPhone', 'sAddress', 'sEmail', 'sPictureUrl']