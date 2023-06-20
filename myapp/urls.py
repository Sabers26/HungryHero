from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('nuevoPlato/', views.nuevo_plato, name='nuevo_plato'),
    path('modificarPlato/<id>', views.modificar_plato, name='modificar_plato'),
    path('eliminarPlato/<id>', views.eliminar_plato, name='eliminar_plato'),
]
