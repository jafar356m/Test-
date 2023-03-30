from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .serializer import MyUserSerializer
from rest_framework import viewsets
from .models import Post
from . serializer import Taskserialzers
from rest_framework.permissions import IsAuthenticated,AllowAny

class MyUserView(generics.CreateAPIView):
    permission_classes=(AllowAny,)
    serializer_class = MyUserSerializer

class Taskviewset(viewsets.ModelViewSet):
    permission_classes=(IsAuthenticated,)
    queryset=Post.objects.filter(publish=True).order_by('-date_created')
    serializer_class=Taskserialzers


class DueTaskviewset(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-date_created').filter(publish=False)
    serializer_class = Taskserialzers

class completedTaskviewset(viewsets.ModelViewSet):
    queryset =Post.objects.all().order_by('-date_created').filter(publish=True)
    serializer_class=Taskserialzers
from django.contrib.auth import login

from rest_framework import permissions
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        
        login(request,user)
        print("user=",request.user)
        return super(LoginAPI, self).post(request, format=None)