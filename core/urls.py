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
    path('register/', registercliente, name='registercliente'),
    path('loginmiembro/', loginmiembro, name='loginmiembro'),
    path('addtipolanzamientos/', addtipolanzamientos, name='addtipolanzamientos'),
    path('generosobjects/', generosobjects, name='generosobjects'),
    path('generosadd/', generosadd, name='generosadd'),
]
