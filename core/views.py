from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group

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

# LOGIN 

def logincliente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Verificar si el usuario es un cliente
            if user.groups.filter(name='clientes').exists():
                # Si el usuario es un cliente, iniciar sesión
                login(request, user)
                return redirect('index')  # Redirigir a la página del cliente
            elif user.groups.filter(name='miembros').exists():
                messages.error(request, 'Solo los clientes pueden iniciar sesión en este sitio.')
                return redirect('index')
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
            return redirect('index')

    return render(request, 'index')  # Renderiza la plantilla de inicio con el modal

def logout_view(request):
    logout(request)
    return redirect('index')  # Redirige a la página de inicio u otra página después de cerrar sesión

def loginmiembro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Verificar si el usuario es un miembro
            if user.groups.filter(name='miembros').exists():
                # Si el usuario es un cliente, iniciar sesión
                login(request, user)
                return redirect('miembrosindex')  # Redirigir a la página del cliente
            elif user.groups.filter(name='clientes').exists():
                messages.error(request, 'Solo los miembros pueden iniciar sesión en este sitio.')
                return redirect('loginmiembros')
        else:
            # Si las credenciales son incorrectas, mostrar un mensaje de error
            messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
            return redirect('loginmiembros')

    return render(request, 'loginmiembros')  # Renderiza la plantilla de inicio con el modal

# REGISTRO

def registercliente(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_confirmation']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('index')
        elif len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('index')
        elif len(username) < 3:
            messages.error(request, 'El nombre de usuario debe tener al menos 3 caracteres.')
            return redirect('index')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('index')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return redirect('index')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            cliente_group = Group.objects.get(name='clientes')
            user.groups.add(cliente_group)
            user.save()
            messages.success(request, 'Usuario creado correctamente')
            return redirect('index')

    return render(request, 'index')

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