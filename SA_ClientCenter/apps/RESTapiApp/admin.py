from django.contrib import admin
from RESTapiApp.models import *

class LineAPI_recordMain(admin.ModelAdmin):
    list_display=('Rstate', 'RstateUsed','Rbackurl','RuserID', 'Rtime',)
    ordering=('-Rtime',)
    search_fields=('Rstate',)

class SMSAPI_recordMain(admin.ModelAdmin):
    list_display=('RSMSid', 'RSMSidUsed','RuserID', 'Rtime', 'RSMS_code',)
    ordering=('-Rtime',)
    search_fields=('RSMSid',)

class AccessAPI_recordMain(admin.ModelAdmin):
    list_display=('Raccess_code','Raccess_time','RuserID')
    ordering=('-Raccess_time',)
    search_fields=('Raccess_code',)

admin.site.register(LineAPI_record, LineAPI_recordMain)
admin.site.register(SMSAPI_record, SMSAPI_recordMain)
admin.site.register(AccessAPI_record, AccessAPI_recordMain)
