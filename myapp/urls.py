from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('nuevoIngrediente/', views.nuevo_ing, name='nuevo_ing')
]
