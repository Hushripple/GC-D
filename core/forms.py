from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LanzamientoForm (ModelForm):
    class Meta:
        model = Lanzamiento
        fields = ['tipoLanzamiento', 'nombreLanzamiento', 'artista', 'fechaLanzamiento', 'genero', 'descripcionLanzamiento','precio', 'imagen']
        widgets = {
            'tipoLanzamiento': forms.Select(attrs={'class': 'form-control'}),
            'nombreLanzamiento': forms.TextInput(attrs={'class': 'form-control'}),
            'artista': forms.Select(attrs={'class': 'form-control'}),
            'fechaLanzamiento': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'genero': forms.Select(attrs={'class': 'form-control'}),
            'descripcionLanzamiento': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        
class TipoLanzamientoForm (ModelForm):
    class Meta:
        model = TipoLanzamiento
        fields = ['nombreTipo']
        widgets = {
            'nombreTipo': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombreTipo'}),
                }

class GeneroMusicalForm(ModelForm):
    class Meta:
        model = GeneroMusical
        fields = ['nombreGenero']

class ArtistaForm (ModelForm):
    class Meta:
        model = Artista
        fields = ['nombreArtista', 'fecha_nacimiento', 'biografia', 'imagen']
        
        widgets = {
            'nombreArtista': forms.TextInput(attrs={'class': 'form-control', 'id': 'id_nombreArtista'}),
            'fecha_nacimiento': forms.DateInput(attrs={'class': 'form-control', 'id': 'id_fecha_nacimiento', 'type': 'date'}),
            'biografia': forms.Textarea(attrs={'class': 'form-control', 'id': 'id_biografia', 'rows': 3}),
        }