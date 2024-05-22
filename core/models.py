from django.db import models

# Create your models here.
    
class TipoLanzamiento(models.Model):
    TIPO_CHOICES = [
        ('single', 'Single'),
        ('album', 'Álbum'),
        ('ep', 'EP'),
    ]

    nombreTipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def __str__(self):
        return dict(self.TIPO_CHOICES)[self.nombreTipo]
    
    class Meta:
        verbose_name = "Tipo de lanzamiento"
        verbose_name_plural = "Tipos de lanzamiento"

class Artista(models.Model):
    nombreArtista = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()
    #imagen = models.ImageField(upload_to=upload_to_artista, null=True, blank=True)

    def __str__(self):
        return self.nombreArtista
    
    class Meta:
        verbose_name = "Artista"
        verbose_name_plural = "Artistas"
    
class GeneroMusical(models.Model):
    nombreGenero = models.CharField(max_length=30)

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

    def __str__(self):
        return self.nombreLanzamiento
    
    def precio_clp(self):
        return "${:,.0f}".format(self.precio).replace(",", ".")
    
    class Meta:
        verbose_name = "Lanzamiento"
        verbose_name_plural = "Lanzamientos"