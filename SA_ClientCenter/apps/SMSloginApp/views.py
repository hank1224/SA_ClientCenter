from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings

import urllib.parse
import urllib.request
import random

from SMSloginApp.forms import SMSForm
from DBmanageApp.models import UserData

def SMS_auth_page(request):
    return render(request, 'SMS_auth.html')

def send_SMS(request):
    if request.method == 'POST':
        phone = request.POST.get('Tphone')
        code=str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
        username = settings.SMS_ACCOUNT
        password = settings.SMS_PASSWORD
        mobile = '0963924024'
        message = "歡迎使用SA_CC，您的驗證碼為："+code+"\n請在 10 分鐘內進行驗證，切勿將驗證碼洩漏他人。"
        print("您的驗證碼："+code)
        message = urllib.parse.quote(message)

        msg = 'username='+username+'&password='+password+'&mobile='+mobile+'&message='+message
        url = 'http://api.twsms.com/json/sms_send.php?'+msg

        # resp = urllib.request.urlopen(url)
        # print(resp.read())
        HttpResponse(message+phone)

def check_phoneNUM():
    try:
        UserData.objects.get_or_create(sPhone="???????????")
        return HttpResponse("此號碼已被人註冊")
    except MultipleObjectsReturned:
        return HttpResponse("此電話有多於一人註冊，請洽客服")
    except ObjectDoesNotExist:
        return HttpResponse("沒人用過")

def check_SMScode(request):
    if request.method == 'POST':
        form = SMSForm(request.POST)
        if form.is_valid():
            verification_code = form.cleaned_data['code']
            # 送出驗證碼並驗證
            ...
    else:
        form = SMSForm()
    return render(request, 'verify.html', {'form': form})