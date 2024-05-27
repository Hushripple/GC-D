from django.db import models
from django import forms

import datetime

# Create your models here.
    
TIPO_APROBACION = [
    ('aprobado', 'Aprobado'),
    ('pendiente', 'Pendiente'),
    ('rechazado', 'Rechazado')
]


class TipoLanzamiento(models.Model):
    nombreTipo = models.CharField(max_length=20)
    aprobado = models.CharField(max_length=20, choices=TIPO_APROBACION, default='pendiente')
    fecha_solicitud = models.DateField(null=True, blank=True, default=datetime.date.today)  

    def __str__(self):
        return self.nombreTipo
    
    class Meta:
        verbose_name = "Tipo de lanzamiento"
        verbose_name_plural = "Tipos de lanzamiento"

class Artista(models.Model):
    nombreArtista = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()
    imagen = models.ImageField(upload_to='artistas/', null=False, blank=False)
    aprobado = models.CharField(max_length=20, choices=TIPO_APROBACION, default='pendiente')
    fecha_solicitud = models.DateField(null=True, blank=True, default=datetime.date.today)  

    def clean_imagen(self):
        imagen = self.cleaned_data.get('imagen')
        if not imagen:
            raise forms.ValidationError("Este campo es obligatorio.")
        return imagen

    def __str__(self):
        return self.nombreArtista
    
    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
    
class GeneroMusical(models.Model):
    nombreGenero = models.CharField(max_length=30)
    aprobado = models.CharField(max_length=20, choices=TIPO_APROBACION, default='pendiente')
    fecha_solicitud = models.DateField(null=True, blank=True, default=datetime.date.today)  

    def __str__(self):
        return self.nombreGenero
    
    class Meta:
        verbose_name = "Género Musical"
        verbose_name_plural = "Géneros Musicales"

class Lanzamiento(models.Model):
    tipoLanzamiento = models.ForeignKey(TipoLanzamiento, on_delete=models.CASCADE)
    nombreLanzamiento = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fechaLanzamiento = models.DateField()
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    descripcionLanzamiento = models.TextField()
    precio = models.IntegerField(default=0)
    imagen = models.ImageField(upload_to='lanzamientos/', null=True, blank=True)
    aprobado = models.CharField(max_length=20, choices=TIPO_APROBACION, default='pendiente')
    fecha_solicitud = models.DateField(null=True, blank=True, default=datetime.date.today)  
    def __str__(self):
        return self.nombreLanzamiento
    
    def precio_clp(self):
        return "${:,.0f}".format(self.precio).replace(",", ".")
    
    class Meta:
        verbose_name = "Lanzamiento"
        verbose_name_plural = "Lanzamientos"


    