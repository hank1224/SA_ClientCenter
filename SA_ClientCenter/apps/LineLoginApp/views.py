from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
import requests


from SA_ClientCenter import settings

callbackurl = settings.CALLBACK_URL

@csrf_exempt
def callback(request):
    if request.method == 'GET':
        Lcode = request.GET.get('code')
        # Lstate = request.GET.get('state') #應該要拿嗎？

        url = "https://api.line.me/oauth2/v2.1/token"
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {
            'grant_type': 'authorization_code',
            'code': Lcode,
            'redirect_uri': callbackurl,
            'client_id': settings.LINE_CHANNEL_ID,
            'client_secret': settings.LINE_CHANNEL_SECRET
        }
        response = requests.post(url, headers=headers, data=data)

        access_token = response.json().get('access_token')
        id_token = response.json().get('id_token')
        # r = get_userData_fromLine(access_token)
        a = Verify_ID_token(id_token)
        return HttpResponse(str(a)+str(id_token))

def Verify_ID_token(id_token):
    url="https://api.line.me/oauth2/v2.1/verify"
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data={
        'id_token': id_token,
        'client_id': settings.LINE_CHANNEL_ID
    }
    response = requests.post(url, headers=headers, data=data)
    return response.status_code,response.json()
        
def get_userData_fromLine(access_token):

    url = "https://api.line.me/oauth2/v2.1/userinfo"
    headers = {'Authorization': access_token}
    response = requests.get(url, headers=headers)
    return response.status_code,response.json()
    print(response.status_code)
    print(response.json())

# /callback?code=x9OkbdE1YabYuzxnCIAH&state=12345abcd


# https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri=https://4776-2001-b400-e332-e89a-1cf9-dc13-67df-dda6.jp.ngrok.io/LineLoginApp/callback&state=12345abcd&scope=profile%20openid%20email&promot=consent&ui_locales=zh-TW