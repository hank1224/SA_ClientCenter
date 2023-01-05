from django.urls import re_path, include
from rest_framework import routers

from RESTapiApp import views, viewsets


router = routers.DefaultRouter()
router.register(r'users', viewsets.UserViewSet)
router.register(r'groups', viewsets.GroupViewSet)

# router.register(r'Line_1', viewsets.Line_1ViewSet, "Line_1 get RState")


# 使用自动URL路由连接我们的API。
# 另外，我们还包括支持浏览器浏览API的登录URL。

urlpatterns = [
    re_path(r'^', include(router.urls)),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path('LineLogin/', views.LineLogin),
    re_path('make_token', views.make_token),

    re_path(r'^Line_1/$', views.Line_1View.as_view()),
    re_path(r'^Line_2/$', views.Line_2View.as_view()),
    re_path(r'^Line_3/$', views.Line_3View.as_view()),
]