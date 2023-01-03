from django.db import models

# lineAPI_1
class getLineURL(models.Model):
    Rstate=models.CharField(max_length=36, blank=False, null=True)
    RTime=models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        verbose_name = u"Line Login URL 要求紀錄"
        verbose_name_plural = verbose_name
    
    # def __str__(self):
    #     return self.sUserID
    # # 讓object預設回傳

# lineAPI_2
class getPK_Line(models.Model):
    Rstate=models.CharField(max_length=36, blank=False, null=True)
    RTime=models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = u"PK by Line login 要求紀錄"
        verbose_name_plural = verbose_name



# Create your models here.