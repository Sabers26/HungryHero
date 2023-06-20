from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('platos/', views.lista_platos, name='lista_platos'),
]
