from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework_jwt.utils import jwt_response_payload_handler
from rest_framework_jwt.serializers import JSONWebTokenSerializer
from .serializer import SerializerUser, RegisterSerializerUser

# Create your views here.

class RegisterUsers(generics.GenericAPIView):

    

    serializer_class = RegisterSerializerUser
    #crear la autenticacion manual de usuario gmail
    def post(self, request, *args, **kwargs):

        validaEmail = User.objects.filter(email=request.data.get('email'))
        print(request.data.get('email'))
        print(validaEmail)
        if not validaEmail:

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.save()

            jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
            jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

            payload = jwt_payload_handler(user)
            token = jwt_encode_handler(payload)
            return Response({
                "user":RegisterSerializerUser(user, context=self.get_serializer_context()).data,
                "token":token,
            })
        else:
            return Response({
                "Error":"Existe un Usuario con esa cuenta de email"
            })


class LoginUsers(APIView):

   
    serializer_class = JSONWebTokenSerializer

    
    def post(self, request):
        
        res = True
        coincide = False
        snippet = User.objects.filter(username=request.data.get('username'))
        if not snippet:
            res = False
        else:
            serializers = SerializerUser(snippet,many=True, context={'request':request}) 
            #comprobar aca de forma manual si el password hasheado de la bd es el mismo que el del usuario ingresa sin hashear
            coincide = check_password(request.data.get('password'),serializers.data[0]['password'])
            serializer = self.serializer_class(data=request.data)

            
        if coincide and res and serializer.is_valid():
            token = serializer.object.get('token')
            response_data = jwt_response_payload_handler(token)
            return Response({
            "data":serializers.data,
            "token":response_data,
            
        })
        else:
            return Response({
                'Type':'Invalid Credentials'
            })