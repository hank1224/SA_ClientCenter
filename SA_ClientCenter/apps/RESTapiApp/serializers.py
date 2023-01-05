from django.contrib.auth.models import User, Group
from rest_framework import serializers, filters
import django_filters
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

class Line_getRbackurlSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rbackurl']

class Line_sendStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineAPI_record
        fields = ['Rstate', 'Rtime',]

