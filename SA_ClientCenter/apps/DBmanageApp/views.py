from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt #資安
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

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

            userdata = UserData.objects.filter(sUserID=request.session['UserID'])
            userauth=""
            for i in userdata:
                userauth = i.sPhoneAuth
            # print(userauth,Phone)
            # print(request.session['UserID'])
            if userauth == True:
                try:
                    UserData.objects.get(sPhone=Phone)
                    # 有一隻這個電話
                    try: 
                        UserData.objects.get(sPhone=Phone, sPhoneAuth=True)
                        # 有驗證過的這隻電話
                        try:
                            UserData.objects.get(sUserID=request.session['UserID'], sPhone=Phone, sPhoneAuth=True)
                            # 是本人的
                            UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                                sAddress=Address, sEmail=Email)
                        except ObjectDoesNotExist:
                            # 驗證過不是本人的
                            return HttpResponseRedirect('/UserInterfaceApp/alert_NOTuniquePhone.html') 
                    except ObjectDoesNotExist: 
                        # 沒有驗證過的這隻電話
                        UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                            sAddress=Address, sEmail=Email)
                    except MultipleObjectsReturned:
                        # 多個驗證過的這隻電話，資料庫有問題
                        HttpResponse("多個驗證過的這隻電話，資料庫有問題")
                except ObjectDoesNotExist:
                    # 沒有這隻電話
                    UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                            sAddress=Address, sEmail=Email)
                except MultipleObjectsReturned:
                    # 有多隻這個電話
                    try:
                        UserData.objects.get(sPhone=Phone, sPhoneAuth=True)
                        # 有一隻驗證過
                        try:
                            UserData.objects.get(sUserID=request.session['UserID'], sPhone=Phone, sPhoneAuth=True)
                            # 驗過過的一隻是本人的
                            UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                                sAddress=Address, sEmail=Email)
                        except ObjectDoesNotExist:
                            # 驗證過的一隻不是本人的
                            return HttpResponseRedirect('/UserInterfaceApp/alert_NOTuniquePhone.html') 
                    except ObjectDoesNotExist:
                        # 都沒有驗證過
                        UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                            sAddress=Address, sEmail=Email)
                    except MultipleObjectsReturned:
                        # 多個驗證過的這隻電話，資料庫有問題
                        HttpResponse("多個驗證過的這隻電話，資料庫有問題")
                return HttpResponseRedirect('/UserInterfaceApp/alert_saved.html')

            elif userauth == False:
                try:
                    UserData.objects.get(sPhone=Phone)
                    # 有一隻這個電話
                    try:
                        UserData.objects.get(sPhone=Phone, sPhoneAuth=True)
                        # 這隻有驗證過
                        return HttpResponseRedirect('/UserInterfaceApp/alert_NOTuniquePhone.html') 
                    except ObjectDoesNotExist:
                        # 這隻沒有驗證過
                        UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                            sAddress=Address, sEmail=Email)
                except ObjectDoesNotExist:
                    # 沒有這個電話
                    UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                            sAddress=Address, sEmail=Email)
                except MultipleObjectsReturned:
                        # 多隻電話
                        try:
                            UserData.objects.get(sPhone=Phone, sPhoneAuth=True)
                            # 只有一隻驗證過
                            return HttpResponseRedirect('/UserInterfaceApp/alert_NOTuniquePhone.html')
                        except ObjectDoesNotExist:
                            # 都沒有驗證過
                            UserData.objects.filter(sUserID=request.session['UserID']).update(sName=Name, sNickName=NickName, sPhone=Phone, \
                                sAddress=Address, sEmail=Email)
                        except MultipleObjectsReturned:
                            # 多個驗證過的這隻電話，資料庫有問題
                            HttpResponse("多個驗證過的這隻電話，資料庫有問題")
                return HttpResponseRedirect('/UserInterfaceApp/alert_saved.html')

    else:
        return login_check(request)
# Create your views here.
