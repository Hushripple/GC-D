from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.urls import reverse
from django.core.serializers import serialize

# Create your views here.
def index (request):
    context = {
        'listaArtistas' : Artista.objects.filter(aprobado='aprobado')[:4],
        'listaLanzamientos' : Lanzamiento.objects.filter(aprobado='aprobado')[:4]
    }

    return render(request, 'core/index.html', context)

def artistas (request):
    auxArtObj = {
        'listaArtObj' : Artista.objects.filter(aprobado='aprobado')
    }

    return render(request, 'core/artistas.html', auxArtObj)

def lanzamientos (request):
    auxLanzObj = {
        'listaLanzObj' : Lanzamiento.objects.filter(aprobado='aprobado')
    }

    return render(request, 'core/lanzamientos.html', auxLanzObj)

def loginmiembros (request):
    return render(request, 'core/miembros/loginMiembros.html')

def miembrosindex(request):
    return render(request, 'core/miembros/miembrosIndex.html')

def addtipolanzamientos (request):
    return render(request, 'core/miembros/tipoLanzamientos/crud/add.html')

def addgeneros (request):
    return render(request, 'core/miembros/generos/crud/add.html')

def adminsindex (request): 
    context = {
        'solicitudes' : Artista.objects.filter(aprobado='pendiente').values('id', 'fecha_solicitud', 'nombreArtista', 'aprobado'),
    }
    return render(request, 'core/admins/adminsIndex.html', context)

def adminSolicitudes (request):
    context = {
        'Artistas' : Artista.objects.filter(aprobado='pendiente'),
        'Lanzamientos' : Lanzamiento.objects.filter(aprobado='pendiente'),
        'Generos' : GeneroMusical.objects.filter(aprobado='pendiente'),
        'TiposLanzamientos' : TipoLanzamiento.objects.filter(aprobado='pendiente')
    }
    
    return render(request, 'core/admins/adminsSolicitudes.html', context)

def adminSolicitudesArtistas (request):
    id = request.GET.get('id')
    artista = Artista.objects.filter(id=id).first()
    context = {
        'Artista' : artista
    }
    return render(request, 'core/admins/adminsSolicitudesArtistas.html', context)

def adminSolicitudesLanzamientos (request):
    id = request.GET.get('id')
    lanzamiento = Lanzamiento.objects.filter(id=id).first()
    context = {
        'Lanzamiento' : lanzamiento
    }
    return render(request, 'core/admins/adminsSolicitudesLanzamientos.html', context)

def adminSolicitudesTipoLanzamientos (request):
    id = request.GET.get('id')
    print(id)
    tipolanzamiento = TipoLanzamiento.objects.filter(id=id).first()
    context = {
        'TipoLanzamiento' : tipolanzamiento
    }
    return render(request, 'core/admins/adminsSolicitudesTipoLanzamientos.html', context)

def adminSolicitudesGeneros (request):
    id = request.GET.get('id')
    genero = GeneroMusical.objects.filter(id=id).first()
    context = {
        'Genero' : genero
    }
    return render(request, 'core/admins/adminsSolicitudesGeneros.html', context)

def adminsaprobar (request):
    if request.method == 'POST':
        print(request.POST)
        id = request.POST.get('id')
        tipo = request.POST.get('tipo')
        estado = request.POST.get('aprobado')
        feedback = request.POST.get('feedback')

        match tipo:
            case 'artista':
                print(request.POST)
                artista = Artista.objects.filter(id=id).first()
                artista.aprobado = estado
                artista.feedback = feedback
                artista.save()
            case 'lanzamiento':
                print(request.POST)
                lanzamiento = Lanzamiento.objects.filter(id=id).first()
                lanzamiento.aprobado = estado
                lanzamiento.feedback = feedback
                lanzamiento.save()
            case 'genero':
                print(request.POST)
                genero = GeneroMusical.objects.filter(id=id).first()    
                genero.aprobado = estado
                genero.save()
            case 'TipoLanzamiento':
                print(request.POST)
                tipolanzamiento = TipoLanzamiento.objects.filter(id=id).first()
                tipolanzamiento.aprobado = estado
                tipolanzamiento.feedback = feedback
                tipolanzamiento.save()

        return redirect('adminsolicitudes')
    return render(request, 'adminsolicitudes')

def loginadmins (request):
    return render(request, 'core/admins/loginAdmins.html')

# LOGIN 

def logincliente(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.groups.filter(name='clientes').exists():
                login(request, user)
                return redirect('index')
            elif user.groups.filter(name='miembros').exists():
                messages.error(request, 'Solo los clientes pueden iniciar sesión en este sitio.')
                return redirect('index')
        else:
            messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
            return redirect('index')

    return render(request, 'index')

def logout_view(request):
    logout(request)
    return redirect('index')  

def loginmiembro(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = User.objects.get(email=email)
            username = user.username
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                if user.groups.filter(name='miembros').exists():
                    login(request, user)
                    return redirect('miembrosindex')
                elif user.groups.filter(name='clientes').exists():
                    messages.error(request, 'Solo los miembros pueden iniciar sesión en este sitio.')
                    return redirect('loginmiembros')
            else:
                messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
                return redirect('loginmiembros')
        
        except User.DoesNotExist:
            messages.error(request, 'No existe un usuario con ese correo electrónico.')
            return redirect('loginmiembros')
    
    return render(request, 'loginmiembros')

def loginadmin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.groups.filter(name='administradores').exists():
                login(request, user)
                return redirect('adminsindex') 
            elif user.groups.filter(name='clientes').exists():
                messages.error(request, 'Solo los administradores pueden iniciar sesión en este sitio.')
                return redirect('loginadmins')
            elif user.groups.filter(name='miembros').exists():
                messages.error(request, 'Solo los administradores pueden iniciar sesión en este sitio.')
        else:
            messages.error(request, 'Credenciales de inicio de sesión incorrectas.')
            return redirect('loginadmins')

    return render(request, 'loginadmins')  

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
    auxTipoObj = {
        'listaTipoObj' : TipoLanzamiento.objects.all()
    }

    return render(request, 'core/miembros/tipoLanzamientos/tipolanzamientosobjects.html', auxTipoObj)

def tipolanzamientosadd(request):
    aux = {
        'form': TipoLanzamientoForm()
    }

    if request.method == 'POST':
        formulario = TipoLanzamientoForm(request.POST)
        print(formulario.is_valid())
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "Tipo lanzamiento guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar el tipo de lanzamiento!"

    return render(request, 'core/miembros/tipoLanzamientos/crud/add.html', aux)

def tipolanzamientosupdate(request, id):
    tipo = TipoLanzamiento.objects.get(id=id)

    if request.method == 'POST':
        formulario = TipoLanzamientoForm(data=request.POST, instance=tipo)
        if formulario.is_valid():
            formulario.save()
            return redirect('tipolanzamientosobjects')
    else:
        formulario = TipoLanzamientoForm(instance=tipo)

    return render(request, 'core/miembros/tipoLanzamientos/crud/update.html', {'form': formulario, 'tipo': tipo})

def tipolanzamientosdelete(request, id):
    tipo = TipoLanzamiento.objects.get(id=id)
    tipo.delete()
    
    return redirect(reverse('tipolanzamientosobjects'))

# ARTISTAS
def artistasobjects(request):
    auxArtObj = {
        'listaArtObj' : Artista.objects.all()
    }

    return render(request, 'core/miembros/artistas/artistasobjects.html', auxArtObj)

def artistasadd(request):
    aux = {
        'form': ArtistaForm()
    }

    if request.method == 'POST':
        formulario = ArtistaForm(request.POST, request.FILES) 
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "Artista guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar el artistal!"

    return render(request, 'core/miembros/artistas/crud/add.html', aux)

def artistasupdate(request, id):
    artista = Artista.objects.get(id=id)

    if request.method == 'POST':
        formulario = ArtistaForm(data=request.POST, instance=artista)
        if formulario.is_valid():
            formulario.save()
            return redirect('artistasobjects')
    else:
        formulario = ArtistaForm(instance=artista)

    return render(request, 'core/miembros/artistas/crud/update.html', {'form': formulario, 'artista': artista})

def artistasdelete(request, id):
    artista = Artista.objects.get(id=id)
    artista.delete()
    
    return redirect(reverse('artistasobjects'))

# LANZAMIENTOS
def lanzamientosobjects(request):
    auxLanzObj = {
        'listaLanzObj' : Lanzamiento.objects.all()
    }

    return render(request, 'core/miembros/lanzamientos/lanzamientosobjects.html', auxLanzObj)

def lanzamientosadd(request):
    aux = {
        'form': LanzamientoForm()
    }

    if request.method == 'POST':
        formulario = LanzamientoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "Lanzamiento guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar el lanzamiento!"

    return render(request, 'core/miembros/lanzamientos/crud/add.html', aux)

def lanzamientosupdate(request, id):
    lanzamientos = Lanzamiento.objects.get(id=id)

    if request.method == 'POST':
        formulario = LanzamientoForm(data=request.POST, instance=lanzamientos)
        if formulario.is_valid():
            formulario.save()
            return redirect('lanzamientosobjects')
    else:
        formulario = LanzamientoForm(instance=lanzamientos)

    return render(request, 'core/miembros/lanzamientos/crud/update.html', {'form': formulario, 'lanzamientos': lanzamientos})

def lanzamientosdelete(request, id):
    lanzamientos = Lanzamiento.objects.get(id=id)
    lanzamientos.delete()
    
    return redirect(reverse('lanzamientosobjects'))


# GÉNERO MUSICAL
def generosobjects(request):
    auxGenObj = {
        'listaGenObj' : GeneroMusical.objects.all()
    }

    return render(request, 'core/miembros/generos/generosobjects.html', auxGenObj)

def generosadd(request):
    aux = {
        'form': GeneroMusicalForm()
    }

    if request.method == 'POST':
        formulario = GeneroMusicalForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Género musical guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar el género musical!"

    return render(request, 'core/miembros/generos/crud/add.html', aux)

def generosupdate(request, id):
    genero = GeneroMusical.objects.get(id=id)

    if request.method == 'POST':
        formulario = GeneroMusicalForm(data=request.POST, instance=genero)
        if formulario.is_valid():
            formulario.save()
            return redirect('generosobjects')  # Redirige a la página de géneros después de la edición
    else:
        formulario = GeneroMusicalForm(instance=genero)

    return render(request, 'core/miembros/generos/crud/update.html', {'form': formulario, 'genero': genero})

def generosdelete(request, id):
    genero = GeneroMusical.objects.get(id=id)
    genero.delete()
    
    return redirect(reverse('generosobjects'))

# ADMINS
def registermiembro(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password_confirmation']

        if password1 != password2:
            messages.error(request, 'Las contraseñas no coinciden.')
            return redirect('adminsindex')
        elif len(password1) < 8:
            messages.error(request, 'La contraseña debe tener al menos 8 caracteres.')
            return redirect('adminsindex')
        elif len(username) < 3:
            messages.error(request, 'El nombre de usuario debe tener al menos 3 caracteres.')
            return redirect('adminsindex')
        elif User.objects.filter(username=username).exists():
            messages.error(request, 'El nombre de usuario ya está en uso.')
            return redirect('adminsindex')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'El correo electrónico ya está en uso.')
            return redirect('adminsindex')
        else:
            user = User.objects.create_user(username=username, email=email, password=password1)
            miembro_group = Group.objects.get(name='miembros')
            user.groups.add(miembro_group)
            user.save()
            messages.success(request, 'Cuenta de miembro creada correctamente')
            return redirect('adminsindex')

    return render(request, 'adminsindex')



