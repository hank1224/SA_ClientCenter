from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from DBmanageApp.models import UserData
from RESTapiApp.models import LineAPI_record
from RESTapiApp.serializers import Line_sendStateSerializer, Line_getBackurlSerializer

from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from RESTapiApp.serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.response import Response


# class Line_getBackurlViewSet(viewsets.ModelViewSet):
#   queryset = UserData.objects.all()
#   serializer_class = Line_getBackurlSerializer
#   permission_classes = (AllowAny,)

# import requests
# url = 'http://example.com/api/wash_user'
# headers = {'Authorization': 'Token 12345'}
# response = requests.get(url, headers=headers)



