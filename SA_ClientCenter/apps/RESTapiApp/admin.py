from django.contrib import admin
from RESTapiApp.models import LineAPI_record

class LineAPI_recordMain(admin.ModelAdmin):
    list_display=('Rstate', 'RstateUsed','RuserID', 'Rtime', 'Rbackurl',)
    ordering=('-Rtime',)
    search_fields=('Rstate',)



admin.site.register(LineAPI_record, LineAPI_recordMain)
