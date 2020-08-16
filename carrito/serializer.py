from rest_framework import serializers
from .models import Carrito, ProductosIDsCantidades


class IdsCantidadesSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductosIDsCantidades
        fields = '__all__'

class CarritoSerializer(serializers.ModelSerializer):


    class Meta:
        model = Carrito
        fields = ('id','idUser','productos_ids','created_at','updated_at')

