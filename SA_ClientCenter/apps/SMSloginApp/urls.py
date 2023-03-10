"""SA_ClientCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path, include
from SMSloginApp import views

urlpatterns = [
    # path('index.html', views.check_phoneNUM),
    path('send_SMS', views.send_SMS),
    path('SMS_auth.html', views.SMS_auth_page),
    path('SMS_sentCode.html', views.SMS_sentCode_page),
    path('SMS_CheckCode', views.SMS_CheckCode),
]
