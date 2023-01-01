from django.contrib import admin
# from apps.DBmanageApp.models import UserData 這樣會報錯！
from DBmanageApp.models import UserData

class UserDataMain(admin.ModelAdmin):
    list_display=('sUserID','sLineID','sName','sPhone','sNickName','sAddress','sPictureUrl')
    search_fields=('sName',)



# Register your models here.
admin.site.register(UserData, UserDataMain)