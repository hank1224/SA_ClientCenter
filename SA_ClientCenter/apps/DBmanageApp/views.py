from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #資安
from django.http import HttpResponse, HttpResponseRedirect

from DBmanageApp.models import UserData
from apps.UserInterfaceApp.views import login_check 


@csrf_exempt
def submitUserData(request):
    if login_check(request) == True:
        if request.method == 'POST':
            data = request.POST
            Name = None if request.POST.get('name') == "" else request.POST.get('name')
            NickName = None if request.POST.get('nickname') == "" else request.POST.get('nickname')
            Phone = None if request.POST.get('phone') == "" else request.POST.get('phone')
            Address = None if request.POST.get('address') == "" else request.POST.get('address')
            Email = None if request.POST.get('email') == "" else request.POST.get('email')
        
        UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
            sAddress=Address, sEmail=Email)
        return HttpResponseRedirect('/UserInterfaceApp/alert_saved.html')
    else:
        return login_check(request)
# Create your views here.
