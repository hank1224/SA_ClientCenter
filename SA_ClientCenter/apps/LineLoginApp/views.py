from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
import requests
from uuid import uuid1 #待測試

from SA_ClientCenter import settings
from LineLoginApp.models import UserData

callbackurl = settings.CALLBACK_URL

def index_page(request):
    reurl = callbackurl
    return render(request, 'index.html', locals())

def in_page(request):
    return render(request, 'in.html')

def session_Update(request):
    if not "SA_CC" in request.session:
        request.session['SA_CC'] = True
        request.session.set_expiry(60*20) #存在20分鐘
    else:
        session_clear(request)
        session_Update(request)

def session_clear(request):
     request.session.clear()

def logout(request):
    session_clear(request)
    return HttpResponseRedirect('/LineLoginApp/index.html')

@csrf_exempt
def callback(request):
    if request.method == 'GET':
        Lcode = request.GET.get('code')
        # Lstate = request.GET.get('state') #用以確定跳轉的網址是同一個，可拿來驗證 = rayIs9ay

        url = "https://api.line.me/oauth2/v2.1/token"
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'ngrok-skip-browser-warning': '7414' #用以跳過ngrok的跳轉頁面，如果不是用ngrok就可以移除
            }
        data = {
            'grant_type': 'authorization_code',
            'code': Lcode,
            'redirect_uri': callbackurl,
            'client_id': settings.LINE_CHANNEL_ID,
            'client_secret': settings.LINE_CHANNEL_SECRET
        }
        response = requests.post(url, headers=headers, data=data)

        access_token = response.json().get('access_token')
        # id_token = response.json().get('id_token')
        # refresh_token = response.json().get('refresh_token')

        getProfileStatus_code, profileJSON = Get_user_profile(access_token)
        # r = Verify_ID_token(id_token)

        if getProfileStatus_code == 200: 
            userId = profileJSON.get('userId')
            try:
                UserData.objects.get(sLineID=userId)
            except MultipleObjectsReturned:
                return HttpResponse("MultipleObjectsReturned錯誤，請洽客服")
            except ObjectDoesNotExist:
                displayName = profileJSON.get('displayName')
                statusMessage = profileJSON.get('statusMessage')
                pictureUrl = profileJSON.get('pictureUrl') #網址後接上 /large /small 可得不同大小的圖
                # produce_UUID = uuid1()
                if pictureUrl =="":
                    pictureUrl = None
                try:
                    UserData.objects.create(sLineID=userId, sName=displayName, sPictureUrl=pictureUrl)
                except:
                    return HttpResponse("寫入資料庫發生問題")
                SA_CC_ID = UserData.objects.get(sLineID=userId)
                session_Update(request)
                HttpResponseRedirect('yourNew')
                # HttpResponseRedirect('') #這裡是第一次註冊的人，網址接到填寫資料頁面
        else:
            return HttpResponse("抓取個人資料發生錯誤")

        SA_CC_ID = UserData.objects.get(sLineID=userId)
        session_Update(request)
        return HttpResponseRedirect('/LineLoginApp/in')

"""
def Verify_ID_token(id_token): #太詳細不需要，都是驗證用資料
    url="https://api.line.me/oauth2/v2.1/verify"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data={
        'id_token': id_token,
        'client_id': settings.LINE_CHANNEL_ID
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json(),response.status_code
"""

def Get_user_profile(access_token): #取得使用者資料
    url = "https://api.line.me/v2/profile"
    headers = {
        'ngrok-skip-browser-warning': '7414', #用以跳過ngrok的跳轉頁面，如果不是用ngrok就可以移除
        'Authorization': 'Bearer '+access_token
        }
    response = requests.get(url, headers=headers)
    return response.status_code,response.json()

# https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri=https://4776-2001-b400-e332-e89a-1cf9-dc13-67df-dda6.jp.ngrok.io/LineLoginApp/callback&state=rayIs9ay&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW