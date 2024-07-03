from django.shortcuts import render, redirect, get_object_or_404
from .models import Empresa, Chofer, Vehiculo, Reserva
from .forms import EmpresaForm, VehiculoForm, ChoferForm, ReservaForm
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render (request, 'inicio.html')

############################################################################

def catalogo(request):
    vehiculos = Vehiculo.objects.all()
    return render (request, 'catalogo.html', {'vehiculos': vehiculos})

def cambiar_estado(request, patenteVehiculo):
    vehiculo = get_object_or_404(Vehiculo, patenteVehiculo=patenteVehiculo)
    action = request.GET.get('action')
    
    if action == 'cancel':
        vehiculo.reservado = False
    else:
        vehiculo.reservado = not vehiculo.reservado

    vehiculo.save()
    return redirect('catalogo')
     

############################################################################

def crear(request):
    if request.method == 'POST':
        vehiculoform = VehiculoForm(request.POST, request.FILES)
        if vehiculoform.is_valid():
            vehiculoform.save()
            return redirect('catalogo')  
    else:
        vehiculoform = VehiculoForm()
    
    return render(request, 'crear.html', {'vehiculoform': vehiculoform})

############################################################################    

def modificar(request, id):
    vehiculo = Vehiculo.objects.get(patenteVehiculo=id) 
    datos = {
        'vehiculoform': VehiculoForm(instance=vehiculo), 
        'vehiculo': vehiculo 
    }
    
    if request.method == 'POST':
        formulario = VehiculoForm(request.POST, request.FILES, instance=vehiculo)
        if formulario.is_valid():
            formulario.save()
            return redirect('catalogo') 
    
    return render(request, 'modificar.html', datos)

############################################################################    

def eliminar(request, id):
    vehiculo = get_object_or_404(Vehiculo, patenteVehiculo=id)
    
    if request.method == 'POST':
        if 'eliminar' in request.POST:
            vehiculo.delete()
            return redirect('catalogo')
        else:
            return redirect('detalle', id=id)
    
    return render(request, 'eliminar.html', {'vehiculo': vehiculo})

############################################################################     

def opciones_admin(request):
    return render (request, 'opciones_admin.html')

############################################################################ 


def catalogo_empresas(request):
    empresas = Empresa.objects.all()
    return render(request, 'catalogo_empresas.html', {'empresas': empresas})

def crear_empresa(request):
    if request.method == 'POST':
        empresaform = EmpresaForm(request.POST)
        if empresaform.is_valid():
            empresaform.save()
            return redirect('catalogo_empresas') 
    else:
        empresaform = EmpresaForm()
    
    return render(request, 'crear_empresa.html', {'empresaform': empresaform})

def eliminar_empresa(request, idEmpresa):
    empresa = get_object_or_404(Empresa, idEmpresa=idEmpresa)
    empresa.delete()
    return redirect('catalogo_empresas')


############################################################################ 

def catalogo_choferes(request):
    choferes = Chofer.objects.all()
    return render(request, 'catalogo_choferes.html', {'choferes': choferes})
 
def crear_chofer(request):
    if request.method == 'POST':
        choferform = ChoferForm(request.POST)
        if choferform.is_valid():
            choferform.save()
            return redirect('catalogo_choferes')  
    else:
        choferform = ChoferForm()
    
    return render(request, 'crear_chofer.html', {'choferform': choferform})


def eliminar_chofer(request, rutChofer):
    chofer = get_object_or_404(Chofer, rutChofer=rutChofer)
    chofer.delete()
    return redirect('catalogo_choferes')

################################################################################

def login(request):
    return render (request, 'login.html')

def cerrar(request):
    logout(request)
    return redirect('inicio')


def registrar(request):
    data={
        'form': RegistroUserForm()
    }
    if request.method=='POST':
        formulario = RegistroUserForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],
                   password=formulario.cleaned_data["password1"])
            login(request, user)
            return redirect('inicio')       
        data["form"]=formulario
        return render(request, 'registration/registrar.html',data)
    
def reservar(request, patenteVehiculo):
    vehiculo = get_object_or_404(Vehiculo, patenteVehiculo=patenteVehiculo)

    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            reserva.vehiculo = vehiculo
            reserva.save()
            vehiculo.reservado = True
            vehiculo.save()
            return redirect('boleta', reserva_id=reserva.id)
    else:
        form = ReservaForm()

    return render(request, 'reservar.html', {'form': form, 'vehiculo': vehiculo})

def boleta(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'boleta.html', {'reserva': reserva})

