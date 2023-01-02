from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt #資安
from DBmanageApp.models import UserData


def login_noAccount_page(request):
    reurl = settings.CALLBACK_URL
    CHANNEL_ID = settings.LINE_CHANNEL_ID
    return render(request, 'login_noAccount.html', locals())

def GDPR_page(request):
    return render(request, 'GDPR.html')

def alert_saved_page(request):
    return render(request, 'alert_saved.html')

def login_Account_page(request):
    return render(request, 'login_Account.html')

def alert_accessNO_page(request):
    return render(request, 'alert_accessNO.html')

def inside_page(request):
    if login_check(request) == True:
        UserData_queryset = UserData.objects.filter(sUserID=request.session['UserID'])
        for queryset in UserData_queryset:
            name = "" if queryset.sName == None else queryset.sName
            nickname = "" if queryset.sNickName == None else queryset.sNickName
            phone = "" if queryset.sPhone == None else queryset.sPhone
            address = "" if queryset.sAddress == None else queryset.sAddress
            email = "" if queryset.sEmail == None else queryset.sEmail
            phoneauth = queryset.sPhoneAuth
        return render(request, 'inside.html', locals())
    else:
        return login_check(request)

def logout(request):
    del request.session['UserID']
    return HttpResponseRedirect('login_noAccount.html')

@csrf_exempt
def Login_and_AddSession(request):
    SA_CC_ID = request.GET.get('SA_CC_ID')
    if 'UserID' in request.session:
        del request.session['UserID']
    request.session['UserID'] = SA_CC_ID
    request.session.modified = True
    request.session.set_expiry(60*20) #存在20分鐘
    return HttpResponseRedirect('inside.html')
    # return HttpResponse(request.session['UserID'])

def login_check(request):
    if not 'UserID' in request.session:
        check_return = HttpResponseRedirect('login_noAccount.html')
    elif 'UserID' in request.session:
        check_return = True
    else:
        check_return = HttpResponse("check_login err")
    return check_return