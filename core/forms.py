from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class LanzamientoForm (ModelForm):
    class Meta:
        model = TipoLanzamiento
        fields = '__all__'
        
class TipoLanzamientoForm (ModelForm):
    class Meta:
        model = TipoLanzamiento
        fields = '__all__'
        widgets = {
            'nombreTipo': forms.Select(attrs={'class': 'form-select'})
                }

class GeneroMusicalForm(ModelForm):
    class Meta:
        model = GeneroMusical
        fields = '__all__'

class ArtistaForm (ModelForm):
    class Meta:
        model = Artista
        fields = '__all__'
