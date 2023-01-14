from django.contrib import admin
from SMSloginApp.models import SMSrecord

class SMSrecordMain(admin.ModelAdmin):
    list_display=('SPhone','STime','SCode','SID',)
    search_fields=('SPhone',)
    ordering=('-STime',)

# Register your models here.

admin.site.register(SMSrecord, SMSrecordMain)