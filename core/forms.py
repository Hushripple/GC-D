from django import forms
from django.forms import ModelForm
from .models import *

class EmpleadoForm (ModelForm):
    class Meta:
        model = Empleado
        # fields = ['rut', 'nombre', 'apellido']
        fields = '__all__'

class TipoEmpleadoForm (ModelForm):
    class Meta:
        model = TipoEmpleado
        fields = '__all__'

class Genero(ModelForm):
    class Meta:
        model = Genero
        fields = '__all__'