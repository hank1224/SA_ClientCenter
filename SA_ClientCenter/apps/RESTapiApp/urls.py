from django.urls import re_path, include
from rest_framework import routers

from RESTapiApp import views, viewsets


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

router.register(r'Line_1', views.Line_1ViewSet, "Line_1")
router.register(r'Line_2', views.Line_2ViewSet, "Line_2")
# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('make_token', views.make_token),
]