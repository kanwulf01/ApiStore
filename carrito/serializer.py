from rest_framework import serializers
from .models import Carrito
from productos.serializer import ProductoSerializer, ProductoImagenesSerializer
from login_auth.serializer import SerializerUser2
from productos.models import Producto
from django.contrib.auth.models import User

#Guarda Carrito 
class CarritoSerializer(serializers.ModelSerializer):

    idUser = SerializerUser2
    productos_ids = ProductoSerializer

    class Meta:
        model = Carrito
        fields = ('id','idUser','productos_ids','created_at','updated_at','activo','cantidad','precio_unidad')
    
#Lista el carrito con serializadores anidados
class CarritoSerializerListaAnidados(serializers.ModelSerializer):

    idUser = SerializerUser2()
    productos_ids = ProductoImagenesSerializer()

    class Meta:
        model = Carrito
        fields = ('id','idUser','productos_ids','created_at','updated_at','activo','cantidad','precio_unidad')

