from django.db import models
# from uuid import uuid4
class LineAPI_record(models.Model):
    Rstate= models.CharField(max_length=36, verbose_name="網址state辨識碼(用以二次請求)")
    RstateUsed=models.BooleanField(default=False, verbose_name="請求UserID與否(第二次握手)") #指二次握手使用過嗎？
    RuserID=models.CharField(max_length=36, blank=False, null=True, verbose_name="個資系統判定的使用者ID")
    Rtime=models.DateTimeField(auto_now=False, auto_now_add=True, verbose_name="第一次請求網址時間")
    Rbackurl=models.CharField(max_length=200, blank=True, null=True, verbose_name="用戶要求line後返回網址")
    
    class Meta:
        verbose_name = u"LineLogin_API 要求紀錄"
        verbose_name_plural = verbose_name
    
    # def __str__(self):
    #     return self.sUserID
    # # 讓object預設回傳

# Create your models here.