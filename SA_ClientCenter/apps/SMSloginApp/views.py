from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import urllib.parse
import urllib.request
import random

from LineLoginApp.models import UserData

def send_SMS(request):
    code=str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
    username = settings.SMS_ACCOUNT
    password = settings.SMS_PASSWORD
    mobile = '0963924024'
    message = "歡迎使用SA_CC，您的驗證碼為："+code+"\n請在 10 分鐘內進行驗證，切勿將驗證碼洩漏他人。"
    print("您的驗證碼："+code)
    message = urllib.parse.quote(message)

    msg = 'username='+username+'&password='+password+'&mobile='+mobile+'&message='+message
    url = 'http://api.twsms.com/json/sms_send.php?'+msg

    resp = urllib.request.urlopen(url)
    print(resp.read())

def check_phoneNUM():
    try:
        UserData.objects.get(sPhone=Tphone)
        return HttpResponse("此號碼已被人註冊")
    except MultipleObjectsReturned:
        return HttpResponse("此電話有多於一人註冊，請洽客服")
    except ObjectDoesNotExist:
        HttpResponse("沒人用過")