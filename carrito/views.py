from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, permissions
from django.contrib.auth import authenticate
from rest_framework_jwt.settings import api_settings
from django.contrib.auth.models import User
from .models import Carrito
from .serializer import CarritoSerializer, CarritoSerializerListaAnidados
from django.db import connection
from collections import OrderedDict 
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
#cursor.execute('select count(*) from "Task_task" where id_categoria_id=%s',[idcategoria])

class CarritoVieSet(generics.GenericAPIView):
    #En este post descuento la cantidad que se quiere agregar al carrito de compras
    serializer_class = CarritoSerializer

    def post(self, request, *args, **kwargs):

        cantidad = request.data.get('cantidad')
        idP = request.data.get('productos_ids')
        precio_u = request.data.get('precio_unidad')
        data = OrderedDict()
        data.update(request.data)
        #request.data._mutable = True
        #le cambio la inmutabilidad al querydict del request Post para alterar el valor
        #de precio unidad ya que se altera por la cantidad que se quiere comprar
        if not request.POST._mutable:
            request.POST._mutable = True

        data['precio_unidad'] = int(cantidad) * int(precio_u)

        with connection.cursor() as cursor:
            #cursor.execute('select count(*) from "Productos_productos" where id_categoria_id=%s',[idcategoria])
            #La siguiente linea upgradea la cantidad del producto real, pero esto ya lo hago, no hace falta la siguiente linea
            #valido si la cantidad es > 0, si no, no se puede descontar
            cursor.execute('update "productos_producto" set cantidad= cantidad - %s where id=%s',[cantidad,idP])
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        carrito = serializer.save()
      

        return Response({
            "carrito":CarritoSerializer(carrito, context=self.get_serializer_context()).data
        })



class CarritoListVieSet(APIView):

    def get(self,request,userId):

        snippet = Carrito.objects.filter(activo='TRUE', idUser=userId)

        if not snippet:
            return Response({"Error":"No existen productos en carrito"})
        else:
            serializer = CarritoSerializerListaAnidados(snippet, many=True, context={'request':request})

        return Response(serializer.data, status=200)

class CarritoProductosComprados(APIView):

    def patch(self, request,pk):

        with connection.cursor() as cursor:
            cursor.execute('update "carrito_carrito" set activo=%s where id=%s',['COMPARDO',pk])
        
        return Response({
            "update":"update",
        })

