from django.urls import path

from . import views

urlpatterns = [
    path('token/', views.LoginUsers.as_view(), name="Token_return"),
    path('register/', views.RegisterUsers.as_view(), name="Registro"),
]