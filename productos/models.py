from django.db import models

# Create your models here.


class Categoria(models.Model):

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    categoria_id = models.ForeignKey(Categoria, related_name="productos", on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    precio_unidad = models.DecimalField(null=True, blank=True, default=None, max_digits=19, decimal_places=0)
    #activo = models.CharField(max_length=50, default='True')

    def __str__(self):
        return self.nombre





class Image(models.Model):

    image = models.FileField(blank=False, null=False)
    producto_id = models.ForeignKey(Producto, related_name="images", on_delete=models.CASCADE)
