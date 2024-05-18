from django import forms
from django.forms import ModelForm
from .models import *

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