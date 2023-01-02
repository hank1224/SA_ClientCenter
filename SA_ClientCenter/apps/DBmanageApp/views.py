from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #資安
from django.http import HttpResponse, HttpResponseRedirect

from DBmanageApp.models import UserData


@csrf_exempt
def submitUserData(request):
    if request.method == 'POST':
        data = request.POST
        Name = None if request.POST.get('name') == "" else request.POST.get('name')
        NickName = None if request.POST.get('nickname') == "" else request.POST.get('nickname')
        Phone = None if request.POST.get('phone') == "" else request.POST.get('phone')
        Address = None if request.POST.get('address') == "" else request.POST.get('address')
        Email = None if request.POST.get('email') == "" else request.POST.get('email')
    
    UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
        sAddress=Address, sEmail=Email)
    return HttpResponseRedirect('/UserInterfaceApp/inside.html')
# Create your views here.
