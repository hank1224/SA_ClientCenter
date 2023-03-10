# Generated by Django 4.1.4 on 2023-01-06 06:01

import RESTapiApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="AccessAPI_record",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "Raccess_code",
                    models.CharField(
                        default=RESTapiApp.models.AccessUUID,
                        editable=False,
                        max_length=43,
                        unique=True,
                        verbose_name="授權驗證碼",
                    ),
                ),
                (
                    "Raccess_time",
                    models.DateTimeField(auto_now_add=True, verbose_name="授權碼啟用時間"),
                ),
                (
                    "RuserID",
                    models.CharField(max_length=43, verbose_name="個資系統判定的使用者ID"),
                ),
            ],
            options={
                "verbose_name": "AccessAPI_API 要求紀錄",
                "verbose_name_plural": "AccessAPI_API 要求紀錄",
            },
        ),
        migrations.CreateModel(
            name="LineAPI_record",
            fields=[
                (
                    "Rstate",
                    models.CharField(
                        default=RESTapiApp.models.StateUUID,
                        editable=False,
                        max_length=42,
                        primary_key=True,
                        serialize=False,
                        verbose_name="網址state辨識碼(用以二次請求)",
                    ),
                ),
                (
                    "RstateUsed",
                    models.BooleanField(
                        default=False, verbose_name="用以請求UserID與否(第二次握手)"
                    ),
                ),
                (
                    "RuserID",
                    models.CharField(
                        max_length=43, null=True, verbose_name="個資系統判定的使用者ID"
                    ),
                ),
                (
                    "Rtime",
                    models.DateTimeField(auto_now_add=True, verbose_name="第一次請求網址時間"),
                ),
                (
                    "Rbackurl",
                    models.CharField(
                        max_length=200, null=True, verbose_name="用戶要求line後返回的絕對網址"
                    ),
                ),
            ],
            options={
                "verbose_name": "LineLogin_API 要求紀錄",
                "verbose_name_plural": "LineLogin_API 要求紀錄",
            },
        ),
        migrations.CreateModel(
            name="SMSAPI_record",
            fields=[
                (
                    "RSMSid",
                    models.CharField(
                        max_length=42,
                        primary_key=True,
                        serialize=False,
                        verbose_name="要求辨識碼(用以二次請求)",
                    ),
                ),
                (
                    "RSMSidUsed",
                    models.BooleanField(
                        default=False, verbose_name="請求過與否(指二次握手使用過嗎？)"
                    ),
                ),
                (
                    "RuserID",
                    models.CharField(
                        max_length=43, null=True, verbose_name="個資系統判定的使用者ID"
                    ),
                ),
                (
                    "Rtime",
                    models.DateTimeField(auto_now_add=True, verbose_name="第一次發送請求時間"),
                ),
                ("Rphone", models.CharField(max_length=10, null=True)),
                (
                    "RSMS_code",
                    models.CharField(max_length=4, null=True, verbose_name="該次簡訊驗證碼"),
                ),
            ],
            options={
                "verbose_name": "SMSLogin_API 要求紀錄",
                "verbose_name_plural": "SMSLogin_API 要求紀錄",
            },
        ),
    ]
