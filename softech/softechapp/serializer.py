from rest_framework import serializers
from .models import MyUser,Post


class MyUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    

    class Meta:
        model = MyUser
        fields = ('name', 'email', 'mobile', 'username', 'password')

    def create(self, validated_data):
        user = MyUser.objects.create_user(**validated_data)
        return user

class Taskserialzers(serializers.ModelSerializer):

    class Meta:
        model=Post
        fields=['id','Title','Descrption','Tags','date_created','publish']

    
        

class PublishPostserializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields=['id','publish']