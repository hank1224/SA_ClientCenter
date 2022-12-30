from django.contrib import admin
# from apps.LineLoginApp.models import UserData 這樣會報錯！
from LineLoginApp.models import UserData

class UserDataMain(admin.ModelAdmin):
    list_display=('sUserID','sLineID','sAccount','sPassword','sName','sPhone','sPictureUrl')
    search_fields=('sName',)



# Register your models here.
admin.site.register(UserData, UserDataMain)