# Generated by Django 4.1.4 on 2023-01-02 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SMSloginApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="smsrecord",
            name="SID",
            field=models.CharField(max_length=36, null=True),
        ),
    ]
