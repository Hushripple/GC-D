from django.db import models

# Create your models here.
    
class TipoLanzamiento(models.Model):
    TIPO_CHOICES = [
        ('single', 'Single'),
        ('album', 'Álbum'),
        ('ep', 'EP'),
    ]

    nombreTipo = models.CharField(max_length=20, choices=TIPO_CHOICES)

    def str(self):
        return dict(self.TIPO_CHOICES)[self.nombreTipo]

class Artista(models.Model):
    nombreArtista = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    biografia = models.TextField()
    #imagen = models.ImageField(upload_to=upload_to_artista, null=True, blank=True)

    def str(self):
        return self.nombreArtista
    
class GeneroMusical(models.Model):
    nombreGenero = models.CharField(max_length=30)

    def str(self):
        return self.nombreGenero

class Lanzamiento(models.Model):
    tipoLanzamiento = models.ForeignKey(TipoLanzamiento, on_delete=models.CASCADE)
    nombreLanzamiento = models.CharField(max_length=50)
    artista = models.ForeignKey(Artista, on_delete=models.CASCADE)
    fechaLanzamiento = models.DateField()
    genero = models.ForeignKey(GeneroMusical, on_delete=models.CASCADE)
    descripcionLanzamiento = models.TextField()
    precio = models.IntegerField(default=0)

    def str(self):
        return self.nombreLanzamiento
    
    def precio_clp(self):
        return "${:,.0f}".format(self.precio).replace(",", ".")