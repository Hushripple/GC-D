from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index (request):
    return render(request, 'core/index.html')

def artistas (request):
    return render(request, 'core/artistas.html')

def lanzamientos (request):
    return render(request, 'core/lanzamientos.html')

def loginmiembros (request):
    return render(request, 'core/miembros/loginMiembros.html')

def miembrosindex(request):
    return render(request, 'core/miembros/miembrosIndex.html')


# TIPO LANZAMIENTOS

def tipolanzamientosobjects(request):
    tipolanzamientos = TipoLanzamiento.objects.all()
    aux = {
        'lista' : tipolanzamientos
    }

    return render(request,'core/miembros/miembrosIndex.html', aux)

def tipolanzamientosadd(request):
    aux = {
        'form'  : TipoLanzamientoForm()
    }

    if request.method == 'POST':
        formulario = TipoLanzamiento(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Tipo de lanzamiento guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar tipo de lanzamiento!"

    return render(request, 'core/miembros/tipoLanzamientos/crud/add.html', aux)

def tipolanzamientosupdate(request, id):
    tipolanzamientos = TipoLanzamiento.objects.get(id=id)
    aux = {
        'form'  : TipoLanzamientoForm(instance=tipolanzamientos)
    }

    if request.method == 'POST':
        formulario = TipoLanzamientoForm(request.POST, instance=tipolanzamientos)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Tipo de lanzamiento actualizado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al actualizar tipo de lanzamiento!"

    return render(request, 'core/miembros/tipoLanzamientos/crud/update.html', aux)

def tipolanzamientosdelete(id):
    tipolanzamientos = TipoLanzamiento.objects.get(id=id)
    tipolanzamientos.delete()

    return redirect(to = 'core/miembros/miembrosIndex.html')


# LANZAMIENTOS

def lanzamientosobjects(request):
    lanzamientos = Lanzamiento.objects.all()
    aux = {
        'lista' : lanzamientos
    }

    return render(request,'core/miembros/miembrosIndex.html', aux)

def lanzamientosadd(request):
    aux = {
        'form'  : LanzamientoForm()
    }

    if request.method == 'POST':
        formulario = Lanzamiento(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Lanzamiento guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar lanzamiento!"

    return render(request, 'core/miembros/lanzamientos/crud/add.html', aux)

def lanzamientosupdate(request, id):
    lanzamientos = Lanzamiento.objects.get(id=id)
    aux = {
        'form'  : LanzamientoForm(instance=lanzamientos)
    }

    if request.method == 'POST':
        formulario = LanzamientoForm(request.POST, instance=lanzamientos)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Lanzamiento actualizado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al actualizar lanzamiento!"

    return render(request, 'core/miembros/lanzamientos/crud/update.html', aux)

def lanzamientosdelete(id):
    lanzamientos = Lanzamiento.objects.get(id=id)
    lanzamientos.delete()

    return redirect(to = "core/miembros/miembrosIndex.html")


# ARTISTAS

def artistasobjects(request):
    artistas = Artista.objects.all()
    aux = {
        'lista' : artistas
    }

    return render(request, 'core/miembros/miembrosIndex.html', aux)

def artistasadd(request):
    aux = {
        'form' : ArtistaForm()
    }

    if request.method == 'POST':
        formulario = Artista(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Artista guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar artista!"

    return render(request, 'core/miembros/artistas/crud/add.html', aux)

def artistasupdate(request, id):
    artistas = Artista.objects.get(id=id)
    aux = {
        'form' : ArtistaForm(instance=artistas)
    }

    if request.method == 'POST':
        formulario = ArtistaForm(request.POST, instance=artistas)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Artista actualizado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al actualizar artista!"

    return render(request, 'core/miembros/artistas/crud/update.html', aux)

def artistasdelete(id):
    artistas = Artista.objects.get(id=id)
    artistas.delete()

    return redirect(to = "core/miembros/miembrosIndex.html")

# GÉNERO MUSICAL

def generosobjects(request):
    generos = GeneroMusical.objects.all()
    aux = {
        'lista' : generos
    }

    return render(request, 'core/miembros/miembrosIndex.html', aux)

def generosadd(request):
    aux = {
        'form' : GeneroMusicalForm()
    }

    if request.method == 'POST':
        formulario = GeneroMusical(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Género musical guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar el género musical!"

    return render(request, 'core/miembros/generos/crud/add.html', aux)

def generosupdate(request, id):
    generos = GeneroMusical.objects.get(id=id)
    aux = {
        'form' : GeneroMusicalForm(instance=generos)
    }

    if request.method == 'POST':
        formulario = GeneroMusicalForm(request.POST, instance=generos)
        if formulario.is_valid():
            formulario.save()
        else:
            aux['form'] = formulario
            aux['msj'] = "Error al actualizar el género musical!"

    return render(request, 'core/miembros/generos/crud/update.html', aux)

def generosdelete(id):
    generos = GeneroMusical.objects.get(id=id)
    generos.delete()

    return redirect(to = "core/miembros/miembrosIndex.html")