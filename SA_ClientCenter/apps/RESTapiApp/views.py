from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

from rest_framework import status, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import bad_request

from RESTapiApp.models import LineAPI_record
from DBmanageApp.models import UserData

from django.contrib.auth.models import User, Group

from RESTapiApp.serializers import UserSerializer, GroupSerializer
from RESTapiApp.serializers import Line_getBackurlSerializer, Line_sendStateSerializer, Line_getStateSerializer, Line_sendUserIDSerializer

from uuid import uuid4


class UserViewSet(viewsets.ModelViewSet):
    """
    允许用户查看或编辑的API路径。
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    允许组查看或编辑的API路径。
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class Line_1ViewSet(viewsets.ModelViewSet):
    queryset = LineAPI_record.objects.all()
    serializer_class = Line_getBackurlSerializer
    permission_classes = (AllowAny,)
    # authentication_classes = [TokenAuthentication]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # self.perform_create(serializer)
        rbackurl = serializer.validated_data['Rbackurl']
        make_uuid = uuid4()
        create_Rstate = LineAPI_record.objects.create(Rstate=make_uuid, Rbackurl=rbackurl)
        Rserializer = Line_sendStateSerializer(instance=create_Rstate)
        Rserializer.is_valid(raise_exception=True)
        # return Response({'Rstate': create_Rstate.Rstate})
        return Response(Rserializer.data)

class Line_2ViewSet(viewsets.ModelViewSet):
    queryset = LineAPI_record.objects.all()
    serializer_class = Line_sendUserIDSerializer
    permission_classes = (AllowAny,)

    def get(request):
        
        serializer = Line_getStateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        rstate = serializer.validated_data['Rstate']
        try:
            getUserID = LineAPI_record.objects.get(Rstate=rstate, RstateUsed=False)
            try:
                LineAPI_record.objects.filter(Rstate=rstate).update(RstateUsed=True)
                # userid = getUserID
                # Rserializer = 

            except:
                return Response({"status_code": 500, "detail": "個資系統出問題，如果一直出現再跟我說"})
        except:
            return Response({"status_code": 409, "detail": "此Rstate已被使用過"})
        
        


def LineLogin(request):
    SA_CC_ID = request.GET.get('SA_CC_ID')
    State = request.GET.get('state')
    LineAPI_record.objects.filter(Rstate=State).update(RuserID=SA_CC_ID)













def make_token(request):
    from rest_framework.authtoken.models import Token
    from django.contrib.auth import get_user_model
    User = get_user_model()
    
    listA = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14']
    test=0
    for A in listA:
        user = User.objects.get(username=A)     
        Token.objects.create(user=user)
        test += 1
    HttpResponse("if 14, Success make token, test= " + str(test) )