from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('artistas/', artistas, name="artistas"), 
    path('lanzamientos/', lanzamientos, name="lanzamientos"), 
    path('loginmiembros/', loginmiembros, name="loginmiembros"),
    path('miembrosindex/', miembrosindex, name="miembrosindex"),
    path('login/', logincliente, name='login'),
    path('logout/', logout_view, name='logout'),
]
