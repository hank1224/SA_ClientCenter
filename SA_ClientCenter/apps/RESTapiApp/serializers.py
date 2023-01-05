from django.contrib.auth.models import User, Group
from rest_framework import serializers
from DBmanageApp.models import UserData
from RESTapiApp.models import *
from uuid import uuid4

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')



class Line_1Serializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rstate','Rtime','Rbackurl',]

class Line_2Serializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = '__all__'
        
class Access_Serializer(serializers.ModelSerializer):
    class Meta:
        model = AccessAPI_record
        fields = '__all__'

class Line_getRbackurlSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rbackurl']
    # Rbackurl = serializers.CharField(max_length=200, required=True, label='用戶要求line後返回網址')
    # def perform_create(self, serializer):
    #     return serializer.save()

class Line_sendStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rstate', 'Rtime',]
    # Rstate = serializers.CharField(max_length=36, label='從Line_1得到的Rstate')
    # Rtime = serializers.DateTimeField(label="第一次發送請求時間")
    # def State_create(self, serializer):
    #     return serializer.save()