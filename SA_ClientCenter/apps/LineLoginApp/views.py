from django.shortcuts import render, redirect
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt #資安
import requests

from SA_ClientCenter import settings
from DBmanageApp.models import UserData

callbackurl = settings.CALLBACK_URL
channel_id = settings.LINE_CHANNEL_ID

def index_page(request):
    reurl = callbackurl
    CHANNEL_ID = channel_id
    alert = request.GET.get('access')
    return render(request, 'index.html', locals())

def in_page(request):
    return render(request, 'in.html')

@csrf_exempt
def callback(request):
    if request.method == 'GET':
        Lcode = request.GET.get('code')
        Lstate = request.GET.get('state') #用以確定跳轉的網址是同一個，可拿來驗證 = rayIs9ay

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

        #拒絕受予權限的話
        print(access_token)

        if access_token == None:
            return HttpResponseRedirect('/UserInterfaceApp/alert_accessNO.html')
            
        # id_token = response.json().get('id_token')
        # refresh_token = response.json().get('refresh_token')

        getProfileStatus_code, profileJSON = Get_user_profile(access_token)
        # r = Verify_ID_token(id_token)

        if getProfileStatus_code != 200: 
            return HttpResponse("抓取個人資料發生錯誤")
        else:
            userId = profileJSON.get('userId')
            try:
                UserData.objects.get(sLineID=userId)
            except MultipleObjectsReturned:
                return HttpResponse("MultipleObjectsReturned錯誤，請洽客服")
            except ObjectDoesNotExist:
                #這裡是第一次註冊的人

                if Lstate != 'rayIs9ay': #外網進來且未註冊
                    a = "<a href='" + settings.NGROK_URL + "/UserInterfaceApp/login_noAccount.html'>前往</a>"
                    return HttpResponse("<h1>您第一次使用SA_ClientCenter服務，請先" + a + "註冊個人資訊，才能繼續使用</h1>")

                displayName = profileJSON.get('displayName')
                statusMessage = profileJSON.get('statusMessage')
                pictureUrl = profileJSON.get('pictureUrl') #網址後接上 /large /small 可得不同大小的圖
                if pictureUrl =="":
                    pictureUrl = None
                try:
                    UserData.objects.create(sLineID=userId, sNickName=displayName, sPictureUrl=pictureUrl)
                except:
                    return HttpResponse("寫入資料庫發生問題")

        SA_CC_ID_data = UserData.objects.filter(sLineID=userId)
        SA_CC_ID =""
        for i in SA_CC_ID_data:
            SA_CC_ID = i.sUserID

        if Lstate != "rayIs9ay": #回傳的state判斷，來源不是此系統，是從其他地方，轉發UserID給RESTapi做返回
            return redirect('/RESTapiApp/LineLogin/?'+'SA_CC_ID='+SA_CC_ID+'&state='+Lstate)

        if Lstate == "rayIs9ay": #來源為本系統，發session給他做登入
            return redirect('/UserInterfaceApp/Login_and_AddSession?'+'SA_CC_ID='+SA_CC_ID)
            
        else:
            return HttpResponse("判斷state發生錯誤，state= "+Lstate)

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

