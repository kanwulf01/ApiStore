from rest_framework import serializers

from .models import Producto, Categoria, Image

#post de productos
class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','categoria_id','cantidad','precio_unidad')


#post de imagenes
class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = ('id','image','producto_id')


#Lista de productos con imagenes, lista productos con muchas imagenes, gracias al related name que esta en image que apunta a producto
class ProductoImagenesSerializer(serializers.ModelSerializer):

    images = ImageSerializer(many=True)

    class Meta:
        model = Producto
        fields = ('id','nombre','descripcion','categoria_id','cantidad','precio_unidad','images')

    def create(self, validated_data):

        images_files = validated_data.pop('images')
        produc_id = Producto.objects.create(**validated_data)
        for image in images_files:
            Image.objects.create(producto_id=produc_id, **image)
        return produc_id

#devuelve categoria con productos anidados, gracias al related name puesto en en el modelo de producto, que apunta al modelo producto, anido los serializadores
class CategoriaSerializer(serializers.ModelSerializer):

    productos = ProductoImagenesSerializer(many=True)

    class Meta:
        model = Categoria
        fields = ('id','nombre','productos')

    def create(self, validated_data):

        productos_files = validated_data.pop('productos')
        cate_id = Categoria.objects.create(**validated_data)
        for produ in productos_files:
            Producto.objects.create(categoria_id=cate_id, **produ)
        return cate_id

#crea una categoria
class CategoriaPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id','nombre')
