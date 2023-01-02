from django.db import models

class SMSrecord(models.Model):
    SID=models.CharField(max_length=36, blank=False, null=True)
    SPhone=models.CharField(max_length=10, blank=False)
    STime=models.DateTimeField(auto_now=False, auto_now_add=True)
    SCode=models.CharField(max_length=4, blank=False, null=True)
    
    class Meta:
        verbose_name = u"簡訊認證紀錄"
        verbose_name_plural = verbose_name
    
    # def __str__(self):
    #     return self.sUserID
    # # 讓object預設回傳


# Create your models here.
