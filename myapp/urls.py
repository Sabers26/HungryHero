from django.urls import path, include
from . import views
from rest_framework import routers

'''router = routers.DefaultRouter()
router.register('plato', views.PlatoSerializer, basename='Plato')'''

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registrar_cliente, name='registrar_cliente'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('platos/', views.lista_platos, name='lista_platos'),
    path('nuevoPlato/', views.nuevo_plato, name='nuevo_plato'),
    path('modificarPlato/<id>', views.modificar_plato, name='modificar_plato'),
    path('eliminarPlato/<id>', views.eliminar_plato, name='eliminar_plato'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
    path('carrito/', views.carrito, name='carrito'),
    path('agregar-carrito/<id_plato>', views.agregar_carrito, name='agregar_carrito'),
    path('eliminar-carrito/<id_plato>', views.eliminar_carrito, name='eliminar_carrito'),
    #path('api/', include(router.urls)),
]
