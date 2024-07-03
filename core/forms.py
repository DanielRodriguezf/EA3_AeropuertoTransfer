from django import forms 
from django.forms import ModelForm
from django.forms import widgets
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vehiculo, Empresa, Chofer, Reserva

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo
        fields = ['patenteVehiculo', 'marca', 'capacidad', 'imagen', 'Chofer', 'Empresa']
        labels = {
            'patenteVehiculo': 'Patente Vehiculo',
            'marca': 'Marca',
            'capacidad': 'Capacidad',
            'imagen': 'Imagen',
            'Chofer': 'Chofer',
            'Empresa': 'Empresa',
        }
        widgets = {
            'patenteVehiculo': forms.TextInput(attrs={'readonly': 'readonly',
                    'class': 'form-control',
                    'placeholder': 'Ingrese Patente Vehiculo',
                    'id': 'patenteVehiculo'
            }),
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese marca Vehiculo',
                    'id': 'marca'
                }
            ),
            'capacidad': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese capacidad Vehiculo',
                    'id': 'capacidad'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'id': 'imagen'
                }
            ),
            'Chofer': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'Chofer'
                }
            ),
            'Empresa': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'Empresa'
                }
            ),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['patenteVehiculo'].disabled = True
            self.fields['patenteVehiculo'].widget.attrs['readonly']=True 
        else:
            self.fields['patenteVehiculo'].widget.attrs.pop('disabled', None)
            self.fields['patenteVehiculo'].widget.attrs.pop('readonly', None)         

##########################################################################################            

class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['idEmpresa', 'nombreEmpresa']
        labels = {
            'idEmpresa': 'ID Empresa',
            'nombreEmpresa': 'Nombre Empresa',
        }
        widgets = {
            'idEmpresa': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese ID Empresa',
                    'id': 'idEmpresa'
                }
            ),
            'nombreEmpresa': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre Empresa',
                    'id': 'nombreEmpresa'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['idEmpresa'].disabled = True
            self.fields['idEmpresa'].widget.attrs['readonly'] = True
        else:
            self.fields['idEmpresa'].widget.attrs.pop('disabled', None)
            self.fields['idEmpresa'].widget.attrs.pop('readonly', None)                   

########################################################################################## 

class ChoferForm(forms.ModelForm):
    class Meta:
        model = Chofer
        fields = ['rutChofer', 'nombreChofer', 'apellidoChofer', 'telefono']
        labels = {
            'rutChofer': 'Rut Chofer',
            'nombreChofer': 'Nombre Chofer',
            'apellidoChofer': 'Apellido Chofer',
            'telefono': 'Teléfono',
        }
        widgets = {
            'rutChofer': forms.NumberInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Rut Chofer',
                    'id': 'rutChofer'
                }
            ),
            'nombreChofer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Nombre Chofer',
                    'id': 'nombreChofer'
                }
            ),
            'apellidoChofer': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Apellido Chofer',
                    'id': 'apellidoChofer'
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese Teléfono',
                    'id': 'telefono'
                }
            ),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance:
            self.fields['rutChofer'].disabled = True
            self.fields['rutChofer'].widget.attrs['readonly'] = True
        else:
            self.fields['rutChofer'].widget.attrs.pop('disabled', None)
            self.fields['rutChofer'].widget.attrs.pop('readonly', None)


class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['nombre', 'rut', 'telefono', 'direccion']         