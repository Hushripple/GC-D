from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('artistas/', artistas, name="artistas"), 
    path('lanzamientos', lanzamientos, name="lanzamientos"), 
    path('loginmiembros', loginmiembros, name="loginmiembros"),
    path('miembrosindex', miembrosindex, name="miembrosindex"), 
]
