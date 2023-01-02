# Generated by Django 4.1.4 on 2023-01-01 22:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UserData",
            fields=[
                (
                    "sUserID",
                    models.CharField(
                        default=uuid.uuid1,
                        max_length=36,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("sLineID", models.CharField(max_length=33, null=True)),
                ("sName", models.CharField(max_length=20, null=True)),
                ("sNickName", models.CharField(max_length=50, null=True)),
                ("sPhone", models.CharField(max_length=20, null=True, unique=True)),
                ("sAddress", models.CharField(max_length=50, null=True)),
                ("sPictureUrl", models.URLField(null=True)),
            ],
            options={
                "verbose_name": "客戶個人資料",
                "verbose_name_plural": "客戶個人資料",
            },
        ),
    ]