from django.db import models
from django.contrib.auth.models import User
from productos.models import Producto


#Debo crear un campo precio ya que este precio es el precio del articulo
#existen 2 opciones para este campo, para calcularlo mediante su cantidad
#opcion 1: lo mando calculado desde el frontend o mando el precio y la cantidad que se quiere
#comprar y hago el calculo en el backend con un update precio


class Carrito(models.Model):

    idUser = models.ForeignKey(User,on_delete=models.CASCADE)
    productos_ids = models.ForeignKey(Producto, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    activo = models.CharField(max_length=30,default='TRUE')
    cantidad = models.IntegerField(default=0)
    precio_unidad = models.IntegerField()


    


