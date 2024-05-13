from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.
def index (request):
    return render(request, 'core/index.html')

def contacto (request):
    return render(request, 'core/contacto.html')

def shop (request):
    return render(request, 'core/shop.html')

@permission_required('core.view_empleado')
def empleados(request):
    empleados = Empleado.objects.all()
    aux = {
        'lista' : empleados
    }

    return render(request,'core/empleados/index.html', aux)

@permission_required('core.add_empleado')
def empleadosadd(request):
    aux = {
        'form'  : EmpleadoForm()
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Empleado guardado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al guardar empleado!"

    return render(request, 'core/empleados/crud/add.html', aux)

@permission_required('core.change_empleado')
def empleadosupdate(request, id):
    empleado = Empleado.objects.get(id=id)
    aux = {
        'form'  : EmpleadoForm(instance=empleado)
    }

    if request.method == 'POST':
        formulario = EmpleadoForm(request.POST, instance=empleado)
        if formulario.is_valid():
            formulario.save()
            aux['msj'] = "¡Empleado actualizado correctamente!"
        else:
            aux['form'] = formulario
            aux['msj'] = "¡Error al actualizar empleado!"

    return render(request, 'core/empleados/crud/update.html', aux)

@permission_required('core.delete_empleado')
def empleadosdelete(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()

    return redirect(to = "empleados")