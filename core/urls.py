from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"), 
    path('shop/', shop, name="shop"),
    path('contacto/', contacto, name="contacto"),
    path('empleados/', empleados, name="empleados"),
    path('empleados/add/', empleadosadd, name="empleadosadd"),
    path('empleados/update/<id>/', empleadosupdate, name="empleadosupdate"),
    path('empleados/delete/<id>/', empleadosdelete, name="empleadosdelete"),
]
