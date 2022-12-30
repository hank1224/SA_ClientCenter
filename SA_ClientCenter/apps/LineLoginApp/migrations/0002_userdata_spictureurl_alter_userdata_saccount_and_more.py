# Generated by Django 4.1.4 on 2022-12-30 16:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ("LineLoginApp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="userdata",
            name="sPictureUrl",
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="sAccount",
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="sPhone",
            field=models.CharField(max_length=20, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="userdata",
            name="sUserID",
            field=models.CharField(
                default=uuid.uuid1, max_length=36, primary_key=True, serialize=False
            ),
        ),
    ]
