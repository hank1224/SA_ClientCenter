from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt #資安
from django .contrib.auth.decorators import login_required


def login_noAccount_page(request):
    reurl = settings.CALLBACK_URL
    CHANNEL_ID = settings.LINE_CHANNEL_ID
    return render(request, 'login_noAccount.html', locals())

def login_Account_page(request):
    return render(request, 'login_Account.html')

def inside_page(request):
    if login_check(request) == True:
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