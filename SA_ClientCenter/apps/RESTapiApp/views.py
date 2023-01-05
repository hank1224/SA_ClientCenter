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

from RESTapiApp.serializers import *

from datetime import timedelta
from django.utils import timezone

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *

import json

class Line_1View(APIView):
    def get(self,request, *args, **kwargs):
        rbackurl = request.GET.get('Rbackurl')
        if not rbackurl:
            return Response({"status_code": 400, "detail": "Rbackurl不得為空"})
        try:
            queryset = LineAPI_record.objects.create(Rbackurl=rbackurl)
            try:
                rstate = queryset.Rstate
                rtime = queryset.Rtime
                return Response({"Rstate": rstate, "Rtime": str(rtime)})
            except:
                return Response({"status_code": 500, "detail": "抓取RESTapi出錯，如果一直出現再跟我說"})
        except:
            return Response({"status_code": 500, "detail": "建立出錯LineAPI_record，如果一直出現再跟我說"})




class Line_2View(APIView):
    def get(self,request, *args, **kwargs):
        rstate = request.GET.get('Rstate')
        try:
            LineAPI_record.objects.get(Rstate=rstate)
            try:
                LineAPI_record.objects.get(Rstate=rstate, RstateUsed=False)
                try:
                    LineAPI_record.objects.filter(Rstate=rstate, RstateUsed=False).update(RstateUsed=True)
                    queryset = LineAPI_record.objects.filter(Rstate=rstate, RstateUsed=True)
                    try:
                        userid = "抓不到RuserID"
                        for i in queryset:
                            userid = i.RuserID
                            if userid:
                                create_Access = AccessAPI_record.objects.create(RuserID=userid)
                                access_code = create_Access.Raccess_code
                                access_time = create_Access.Raccess_time
                                return Response({'RuserID':userid, 'Raccess_code': access_code, 'Raccess_time': access_time})      
                    except:
                        return Response({"status_code": 500, "detail": "建立Access_code出錯，如果一直出現再跟我說"})
                except:
                    return Response({"status_code": 500, "detail": "更新RstateUsed出錯，如果一直出現再跟我說"})
            except ObjectDoesNotExist:
                return Response({"status_code": 409, "detail": "此Rstate已被使用"})
        except ObjectDoesNotExist:
            return Response({"status_code": 404, "detail": "找不到此Rstate"})


class Line_3View(APIView):
    def get(self,request, *args, **kwargs):
        raccess_code = request.GET.get('Raccess_code')
        now = timezone.now()
        earlier = now - timedelta(minutes=10)
        try:
            AccessAPI_record.objects.get(Raccess_code=raccess_code)
            try:
                AccessAPI_record.objects.get(Raccess_time__gte=earlier, Raccess_code=raccess_code)
                queryset = AccessAPI_record.objects.filter(Raccess_time__gte=earlier, Raccess_code=raccess_code)
                userid = "抓不到sUserID"
                for i in queryset:
                    userid=i.RuserID
                try:
                    UserData.objects.get(sUserID=userid)
                    try:
                        Bqueryset = UserData.objects.filter(sUserID=userid)
                        LineID="抓不到"
                        Name="抓不到"
                        NickName = "抓不到"
                        Phone="抓不到"
                        PhoneAuth="抓不到"
                        Address="抓不到"
                        Email="抓不到"
                        PictureUrl="抓不到"
                        for i in Bqueryset:
                            LineID = i.sLineID
                            Name = i.sName
                            NickName = i.sNickName
                            Phone = i.sPhone
                            PhoneAuth = i.sPhoneAuth
                            Address = i.sAddress
                            Email = i.sEmail
                            PictureUrl = i.sPictureUrl
                        return Response({
                            "sUser": userid, 
                            "sLineID": LineID,
                            "sName": Name,
                            "NickName": NickName,
                            "sPhone": Phone,
                            "shoneAuth": PhoneAuth,
                            "sAddress": Address,
                            "sEmail": Email,
                            "sPictureURL": PictureUrl,
                            })
                    except:
                        return Response({"status_code": 500, "detail": "產生資料發生問題"})
                except ObjectDoesNotExist:
                    return Response({"status_code": 404, "detail": "UserData找不到個人資料"})
            except ObjectDoesNotExist:
                return Response({"status_code": 409, "detail": "此Raccess_code已過期"})
        except ObjectDoesNotExist:
            return Response({"status_code": 404, "detail": "找不到此Raccess_code"})








def LineLogin(request):
    SA_CC_ID = request.GET.get('SA_CC_ID')
    State = request.GET.get('state')
    try:
        LineAPI_record.objects.filter(Rstate=State).update(RuserID=SA_CC_ID)
    except ObjectDoesNotExist:
        return HttpResponse("找不到此State")
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