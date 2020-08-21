from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings

class SerializerUser(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username','first_name','last_name','email','password','last_login','is_active','date_joined')
        read_only_fields = ('email', 'first_name','last_name','id','is_active','date_joined','last_login')

class SerializerUser2(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username')


class RegisterSerializerUser(serializers.ModelSerializer):
    class Meta:

        model = User
        fields = ('id','username','first_name','last_name','password','email' )
     #   extra_kwars = {'password':{'write_only':True}}


    def create(self,validated_data):
        print("PINTAAAA"+str(validated_data))
        user = User.objects.create_user(**validated_data)
        return user
           
      #  read_only_fields = ('email', )