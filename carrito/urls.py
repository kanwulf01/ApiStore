from django.urls import path

from . import views

urlpatterns = [
    path('add/', views.CarritoVieSet.as_view(), name="registro carrito"),
    path('lista/<int:userId>/',views.CarritoListVieSet.as_view(), name="lista carrito"),
    path('comprados/<int:pk>/',views.CarritoProductosComprados.as_view(), name="carrito comprados"),
]

