from django.shortcuts import render

from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage, TextMessage, QuickReply, QuickReplyButton, MessageAction
from SA_ClientCenter import settings

Line_bot_api = LineBotApi(settings.LINE_CHANNEL_ID)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()

        for event in events:
            if isinstance(event, MessageEvent):
                if isinstance(event.message, TextMessage):
                    mtext = event.message.text

# Create your views here.

def login(requset):
    return HttpResponse("510")
    r = requset.post('https://access.line.me/oauth2/v2.1/authorize?response_type=code&client_id=1657781063&redirect_uri=/////&state=12345abcd&scope=profile%20openid%20email')