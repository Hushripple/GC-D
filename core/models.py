from django.db import models

# Create your models here.

class Genero (models.Model):
    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

class TipoEmpleado(models.Model):
    descripcion = models.CharField(max_length = 40)
    

    def __str__(self):
        return self.descripcion

class Empleado(models.Model):
    rut = models.CharField(max_length = 12)
    nombre = models.CharField(max_length = 40)
    apellido = models.CharField(max_length = 40)
    edad = models.IntegerField(default = 0)
    direccion = models.CharField(max_length = 60)
    telefono = models.CharField(max_length = 20)
    habilitado = models.BooleanField(default = True)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE, default=1)
    tipo = models.ForeignKey(TipoEmpleado, on_delete=models.CASCADE)
    fecha_ingreso = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nombre
    
