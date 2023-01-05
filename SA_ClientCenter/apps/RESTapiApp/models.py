from django.db import models
from uuid import uuid4

def StateUUID():
    return "State-"+str(uuid4())

def SMSUUID():
    return "SMS-"+str(uuid4())

def AccessUUID():
    return "Access-"+str(uuid4())

class LineAPI_record(models.Model):
    Rstate= models.CharField(max_length= 42, primary_key=True, default=StateUUID, editable = False, verbose_name="網址state辨識碼(用以二次請求)")
    RstateUsed=models.BooleanField(default=False, verbose_name="用以請求UserID與否(第二次握手)")
    RuserID=models.CharField(max_length=43, blank=False, null=True, verbose_name="個資系統判定的使用者ID")
    Rtime=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="第一次請求網址時間")
    Rbackurl=models.CharField(max_length=200, blank=False, null=False, verbose_name="用戶要求line後返回的絕對網址")

    class Meta:
        verbose_name = u"LineLogin_API 要求紀錄"
        verbose_name_plural = verbose_name
    

class SMSAPI_record(models.Model):
    RSMSid= models.CharField(max_length= 42, primary_key=True, default=SMSUUID, editable = False, verbose_name="要求辨識碼(用以二次請求)")
    RSMSidUsed=models.BooleanField(default=False, verbose_name="請求過與否(指二次握手使用過嗎？)")
    RuserID=models.CharField(max_length=43, blank=False, null=True, verbose_name="個資系統判定的使用者ID")
    Rtime=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="第一次發送請求時間")
    RSMS_code=models.CharField(max_length=4, verbose_name="該次簡訊驗證碼")
    
    class Meta:
        verbose_name = u"SMSLogin_API 要求紀錄"
        verbose_name_plural = verbose_name
    

class AccessAPI_record(models.Model):
    Raccess_code=models.CharField(max_length=43, unique=True, default=AccessUUID, editable=False, verbose_name="授權驗證碼")
    Raccess_time=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="授權碼啟用時間")
    RuserID=models.CharField(max_length=43, blank=False, null=False, verbose_name="個資系統判定的使用者ID")
    class Meta:
        verbose_name = u"AccessAPI_API 要求紀錄"
        verbose_name_plural = verbose_name
