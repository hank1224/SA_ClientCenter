from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.views.decorators.http import require_http_methods
from django.conf import settings

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

import urllib.parse
import urllib.request
import random
import json

class Line_1View(APIView):
    def get(self,request, *args, **kwargs):
        rbackurl = request.GET.get('Rbackurl')
        if not rbackurl:
            return Response({"detail": "Rbackurl不得為空"},status=status.HTTP_400_BAD_REQUEST)
        try:
            queryset = LineAPI_record.objects.create(Rbackurl=rbackurl)
            try:
                rstate = queryset.Rstate
                rtime = queryset.Rtime
                return Response({"Rstate": rstate, "Rtime": str(rtime)})
            except:
                return Response({"detail": "抓取RESTapi出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except:
            return Response({"detail": "建立出錯LineAPI_record，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


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
                            else:
                                return Response({"detail": "抓不到RuserID，使用者還未使用State給line做登入，此State已作廢"},status=status.HTTP_406_NOT_ACCEPTABLE)    
                    except:
                        return Response({"detail": "建立Access_code出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except:
                    return Response({"detail": "更新RstateUsed出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except ObjectDoesNotExist:
                return Response({"detail": "此Rstate已被使用"},status=status.HTTP_409_CONFLICT)
        except ObjectDoesNotExist:
            return Response({"detail": "找不到此Rstate"},status=status.HTTP_404_NOT_FOUND)


class Access_View(APIView):
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
                        return Response({"detail": "產生資料發生問題"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except ObjectDoesNotExist:
                    return Response({"detail": "UserData找不到個人資料"},status=status.HTTP_404_NOT_FOUND)
            except ObjectDoesNotExist:
                return Response({"detail": "此Raccess_code已過期"},status=status.HTTP_409_CONFLICT)
        except ObjectDoesNotExist:
            return Response({"detail": "找不到此Raccess_code"},status=status.HTTP_404_NOT_FOUND)


class SMS_1View(APIView):
    def get(self,request, *args, **kwargs):
        rphone = request.GET.get('Rphone')
        phone = str(rphone)
        if len(phone) != 10 or rphone.startswith('09') != True:
            return Response({"status_code": 400, "detail": "Rphone格式不接受，需有10碼且是 09 開頭"})
        else:    
            try:
                UserData.objects.get(sPhone=rphone, sPhoneAuth=True)
                try:
                    rsmsid, code = send_SMS(rphone)
                    # queryset = SMSAPI_record.objects.create(Rphone=rphone)
                    try:
                        # rsmsid = queryset.RSMSid
                        # rtime = queryset.Rtime
                        return Response({"RSMSid": rsmsid})
                    except:
                        return Response({"detail": "抓取RESTapi出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except:
                    return Response({"detail": "建立出錯SMSAPI_record，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except ObjectDoesNotExist:
                return Response({"detail": "這隻電話尚未在本系統實名註冊"},status=status.HTTP_404_NOT_FOUND)

class SMS_2View(APIView):
    def get(self,request, *args, **kwargs):
        rsmsid = request.GET.get('RSMSid')
        rsms_code = request.GET.get('RSMS_code')
        try:
            SMSAPI_record.objects.get(RSMSid=rsmsid)
            try:
                SMSAPI_record.objects.get(RSMSid=rsmsid, RSMSidUsed=False)
                try:
                    SMSAPI_record.objects.filter(RSMSid=rsmsid, RSMSidUsed=False).update(RSMSidUsed=True)
                    queryset = SMSAPI_record.objects.filter(RSMSid=rsmsid, RSMSidUsed=True)
                    try:
                        inside_SMSode = "抓不到"
                        rphone=""
                        for i in queryset:
                            rphone = i.Rphone
                            inside_SMSode = i.RSMS_code
                            if rsms_code == inside_SMSode:
                                try:
                                    UserData.objects.get(sPhone=rphone, sPhoneAuth=True)
                                    try:
                                        querysetU = UserData.objects.filter(sPhone=rphone, sPhoneAuth=True)
                                        userid="抓不到"
                                        for i in querysetU:
                                            userid = i.sUserID
                                        create_Access = AccessAPI_record.objects.create(RuserID=userid)
                                        access_code = create_Access.Raccess_code
                                        access_time = create_Access.Raccess_time
                                        return Response({'RuserID':userid, 'Raccess_code': access_code, 'Raccess_time': access_time}) 
                                    except:
                                        return Response({"detail": "建立Access_code出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                                except ObjectDoesNotExist:
                                    return Response({"detail": "驗證成功，但找不到已驗證的此號碼"},status=status.HTTP_404_NOT_FOUND)
                            else:
                                return Response({"detail": "驗證失敗"},status=status.HTTP_406_NOT_ACCEPTABLE)
                    except:
                        return Response({"detail": "建立Access_code出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                except:
                    return Response({"detail": "更新RSMSidUsed出錯，如果一直出現再跟我說"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except ObjectDoesNotExist:
                return Response({"detail": "此RSMSid已被使用"},status=status.HTTP_409_CONFLICT)
        except ObjectDoesNotExist:
            return Response({"detail": "找不到此RSMSid"},status=status.HTTP_404_NOT_FOUND)


def LineLogin(request): # 從linelogin app  view接入
    SA_CC_ID = request.GET.get('SA_CC_ID')
    State = request.GET.get('state')
    try:
        LineAPI_record.objects.filter(Rstate=State).update(RuserID=SA_CC_ID)
    except ObjectDoesNotExist:
        return HttpResponse("找不到此State")
    getBackurl = LineAPI_record.objects.get(Rstate=State)
    backurl = getBackurl.Rbackurl
    return HttpResponseRedirect(backurl)


def send_SMS(rphone):
        code=str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
        username = settings.SMS_ACCOUNT
        password = settings.SMS_PASSWORD
        mobile = rphone
        make_uuid = str(uuid4())
        a = "RSMSid-"
        rsmsid = ''.join([a, make_uuid])
        message = "歡迎使用SA_CC，您的驗證碼為："+code+"\n請在 10 分鐘內進行驗證，切勿將驗證碼洩漏他人。\n此次驗證編號"+make_uuid[-5:]
        print("您的驗證碼："+code)
        message = urllib.parse.quote(message)

        msg = 'username='+username+'&password='+password+'&mobile='+mobile+'&message='+message
        url = 'http://api.twsms.com/json/sms_send.php?'+msg

        # 這行掛上去就真的會發簡訊！
        # resp = urllib.request.urlopen(url)
        # 這行掛上去就真的會發簡訊！

        API_SMSrecord = SMSAPI_record.objects.create(RSMSid=rsmsid, Rphone=rphone, RSMS_code=code)

        return rsmsid, code

        


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