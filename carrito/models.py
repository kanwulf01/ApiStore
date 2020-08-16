from django.db import models
from django.contrib.auth.models import User



class ProductosIDsCantidades(models.Model):
    
    productID =  models.IntegerField()
    cantidad = models.IntegerField()


class Carrito(models.Model):

    idUser = models.OneToOneField(User, related_name="carrito", on_delete=models.CASCADE)
    productos_ids = models.ForeignKey(ProductosIDsCantidades, related_name="idscantidades", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

