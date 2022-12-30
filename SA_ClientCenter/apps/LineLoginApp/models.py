from django.db import models
from uuid import uuid1

class UserData(models.Model):
    sUserID=models.CharField(max_length=36, primary_key=True, default=uuid1)
    sLineID=models.CharField(max_length=33, blank=False, null=True)
    sAccount=models.CharField(max_length=20, blank=False, null=True, unique=True)
    sPassword=models.CharField(max_length=20, blank=False, null=True)
    sName=models.CharField(max_length=30, blank=False, null=True)
    sPhone=models.CharField(max_length=20, blank=False, null=True, unique=True)
    sPictureUrl=models.URLField(max_length=200, blank=False, null=True)

    class Meta:
        verbose_name = u"客戶個人資料"
        verbose_name_plural = verbose_name
    
    def __str__(self):
        return self.sUserID
    # 讓object預設回傳


# Create your models here.
