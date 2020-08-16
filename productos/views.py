from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db import connection
from .serializer import CategoriaPostSerializer, ProductoSerializer, ProductoImagenesSerializer, CategoriaSerializer, ImageSerializer
from .models import Producto, Categoria, Image
from rest_framework import generics, permissions
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.views import APIView


# Create your views here.

class CategoryViewSet(generics.GenericAPIView):

    
    serializer_class = CategoriaPostSerializer

    def post(self,request,*args,**kwargs):

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        categori = serializer.save()
        return Response({
            "categoria":CategoriaPostSerializer(categori, context=self.get_serializer_context()).data
        })

class ProductosPostViewSet(generics.GenericAPIView):

    serializer_class = ProductoSerializer

    def post(self,request, *args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producto = serializer.save()
        return Response({
            "producto":ProductoSerializer(producto, context=self.get_serializer_context()).data
        })

class ImagesPostViewSet(generics.GenericAPIView):

    serializer_class = ImageSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        images = serializer.save()
        return Response({
            "images":ImageSerializer(images, context=self.get_serializer_context()).data
        })


class ListProductos(generics.ListAPIView):

    queryset = Producto.objects.all()
    serializer_class = ProductoImagenesSerializer
    #queryset.delete()

class ListCategorias(generics.ListAPIView):

    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #queryset.delete()

class ListaImages(generics.ListAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    #queryset.delete()

#Updatea la cantidad de un producto que ingreso al carrito de compras
class UpdateProductos(APIView):

    def patch(self, request,pk,cantidad):

        model = get_object_or_404(Producto,pk=pk)
        data = {'cantidad':model.cantidad-int(cantidad)}

        serializer = ProductoSerializer(model, data=data, partial=True, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else: 
            return Response("error")

class RestauraProductos(APIView):
    def patch(self,request,pk,cantidad):
        model = get_object_or_404(Producto,pk=pk)
        data = {'cantidad':model.cantidad+int(cantidad)}

        serializer = ProductoSerializer(model, data=data, partial=True, context={'request':request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response("error")



class getPaginationReturn(APIView):

    

    def get(self, request):

        with connection.cursor() as cursor:

            cursor.execute('select count(*) from "productos_producto"')
            row = cursor.fetchone()

        return Response(row)


# retorna temas de una categoria por id, recibe de parametros:
# el numero de paginas de toda la paginacion
# el numero de paginacion seleccionado
# la id de la categoria
class PaginationResponse(APIView):



    def get(self, request, paginationpages,paginationpage):
        hasta = 6
        desde = 0


        with connection.cursor() as cursor:
            #cursor.execute('select count(*) from "Productos_productos" where id_categoria_id=%s',[idcategoria])

            cursor.execute('select count(*) from "productos_producto"')
            row = cursor.fetchone()
            intcantidad = int(row[0])
        print("PINTA EL TAMAÑO DE LAS TAREAS SEGUN EL ID DE LA CATEGORIA"+str(intcantidad))

        for i in range(1,paginationpages+1):

            if i == paginationpage:
                print("imprime el if del for"+str(i))
                if hasta <= intcantidad:
                    snippet = Producto.objects.all()[desde:hasta]
                    serializer = ProductoImagenesSerializer(snippet, many=True, context={'request':request})
                    desde = hasta
                    hasta = hasta + 6
                    print("entro acaaaaa")
                    return Response(serializer.data)
                else:
                    diferencia_hasta_sizeitems = hasta - intcantidad
                    number = (hasta) - (hasta-6)
                    falta = number - diferencia_hasta_sizeitems
                    hasta = (hasta-6) + falta
                    snippets = Producto.objects.all()[desde:hasta]
                    print("entro al else")
                    serializer = ProductoImagenesSerializer(snippets, many=True, context={'request':request})
                    return Response(serializer.data)
            else:
                if hasta <= intcantidad:
                    desde = hasta
                    hasta = hasta + 6
                else:
                    return Response({"no entra":"no funciona"})
                    #print("no hacer nada")
