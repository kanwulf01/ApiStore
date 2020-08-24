from rest_framework import routers

from . import views
from django.urls import path

urlpatterns = [
    path('CreateCategorias/', views.CategoryViewSet.as_view(), name="Crea Categorias"),
    path('CreateProductos/', views.ProductosPostViewSet.as_view(), name="Crea Productos"),
    path('SafeImages/', views.ImagesPostViewSet.as_view(), name="images"),
    path('listaAll/', views.ListCategorias.as_view(), name="Todo"),
    path('listaProductos/', views.ListProductos.as_view(), name="Productos"),
    path('listaimages/', views.ListaImages.as_view(), name="Images"),
    path('edita/<int:pk>/<int:cantidad>/', views.UpdateProductos.as_view(), name="Upgradea un producto"),
    path('restaura/<int:pk>/<int:cantidad>/',views.RestauraProductos.as_view(), name="restaura producto"),
    path('getCantidadTaskbyCat/', views.getPaginationReturn.as_view(), name="cantidadtask"),  
    path('testpagination/<int:paginationpages>/<int:paginationpage>/', views.PaginationResponse.as_view(), name="testpagination"),
    path('getProducto/<int:pk>/', views.GetProductoID.as_view(), name="Find Producto"),

]
