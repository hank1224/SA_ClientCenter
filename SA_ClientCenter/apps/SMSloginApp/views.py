from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt #資安
from django.conf import settings

import urllib.parse
import urllib.request
import random
from uuid import uuid4

from DBmanageApp.models import UserData
from SMSloginApp.models import SMSrecord


def SMS_auth_page(request):
    return render(request, 'SMS_auth.html')

@csrf_exempt
def SMS_sentCode_page(request):
    if request.method == 'POST': #第一次進來
        Tphone = request.POST.get('Tphone')
        if len(Tphone) != 10 or Tphone.startswith('09') != True:
            vaildPhone = False
            return render(request, 'SMS_auth.html', locals())

        make_uuid = send_SMS(Tphone)

        return render(request, 'SMS_sentCode.html', locals())

def send_SMS(Tphone):
        code=str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))+str(random.randint(0, 9))
        username = settings.SMS_ACCOUNT
        password = settings.SMS_PASSWORD
        mobile = Tphone
        make_uuid = str(uuid4())
        message = "歡迎使用SA_CC，您的驗證碼為："+code+"\n請在 10 分鐘內進行驗證，切勿將驗證碼洩漏他人。\n此次驗證編號"+make_uuid[-5:]
        print("個資系統登入驗證碼："+code)
        message = urllib.parse.quote(message)

        msg = 'username='+username+'&password='+password+'&mobile='+mobile+'&message='+message
        url = 'http://api.twsms.com/json/sms_send.php?'+msg

        # 這行掛上去就真的會發簡訊！
        # resp = urllib.request.urlopen(url)
        # 這行掛上去就真的會發簡訊！

        new_SMSrecord = SMSrecord.objects.create(SID=make_uuid, SCode=code, SPhone=Tphone)
        return make_uuid

@csrf_exempt
def SMS_CheckCode(request):
    if request.method == 'POST':
        phone = request.POST.get('Tphone')
        code = request.POST.get('code')
        make_uuid = request.POST.get('make_uuid')
        data = SMSrecord.objects.filter(SID=make_uuid)
        dbcode=""
        for i in data:
            dbcode = i.SCode
        if code != dbcode:
            vaildCode = False
            return render(request, 'SMS_auth.html', locals()) #驗證失敗
        else:
            try: #檢查是否新來的
                UserData.objects.get(sPhone=phone, sPhoneAuth=True)
            except MultipleObjectsReturned:
                return HttpResponse("MultipleObjectsReturned錯誤，請洽客服")
            except ObjectDoesNotExist:
                #這裡是第一次註冊的人
                try:
                    UserData.objects.create(sPhone=phone, sPhoneAuth=True)
                except:
                    return HttpResponse("寫入資料庫發生問題")

        SA_CC_ID_data = UserData.objects.filter(sPhone=phone, sPhoneAuth=True)
        SA_CC_ID =""
        for i in SA_CC_ID_data:
            SA_CC_ID = i.sUserID
        return redirect('/UserInterfaceApp/Login_and_AddSession?'+'SA_CC_ID='+SA_CC_ID)
    else:
        return HttpResponse("非POST表單")



