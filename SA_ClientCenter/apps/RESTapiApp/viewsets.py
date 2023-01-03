from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

from DBmanageApp.models import UserData
from RESTapiApp.models import LineAPI_record
from RESTapiApp.serializers import Line_getBackurlSerializer , Line_getStateSerializer

from uuid import uuid4


class DataViewSet(viewsets.ModelViewSet):
    queryset = LineAPI_record.objects.all()
    serializer_class = Line_getBackurlSerializer

    def create(self, request):
        # 取得使用者提交的資料
        data = request.data

        # 建立新資料
        new_data = Data(uuid=uuid.uuid4(), data=data)
        new_data.save()

        # 使用序列化器處理資料
        serializer = DataSerializer(new_data)
        return Response(serializer.data)




# class Wash_UserViewSet(viewsets.ModelViewSet):
#   queryset = UserData.objects.all()
#   serializer_class = Wash_UserSerializer
#   permission_classes = (IsAuthenticated,)
#   authentication_classes = (TokenAuthentication,)

# import requests
# url = 'http://example.com/api/wash_user'
# headers = {'Authorization': 'Token 12345'}
# response = requests.get(url, headers=headers)



