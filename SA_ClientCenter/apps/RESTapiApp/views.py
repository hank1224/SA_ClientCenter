from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.decorators.http import require_http_methods

from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import bad_request

from RESTapiApp.models import LineAPI_record
from DBmanageApp.models import UserData

from django.contrib.auth.models import User, Group

from RESTapiApp.serializers import *

from uuid import uuid4



def LineLogin(request):
    SA_CC_ID = request.GET.get('SA_CC_ID')
    State = request.GET.get('state')
    try:
        LineAPI_record.objects.filter(Rstate=State).update(RuserID=SA_CC_ID, RstateUsed=True)
    except ObjectDoesNotExist:
        return HttpResponse("該State已被使用，或找不到此State")
    getBackurl = LineAPI_record.objects.get(Rstate=State)
    backurl = getBackurl.Rbackurl
    return HttpResponseRedirect(backurl)

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