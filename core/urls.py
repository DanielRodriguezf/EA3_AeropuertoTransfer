from django.urls import path
from . import views

urlpatterns=[
    path('', views.inicio, name="inicio"),
    path('catalogo/', views.catalogo, name="catalogo"),
    path('cambiar_estado/<str:patenteVehiculo>/', views.cambiar_estado, name='cambiar_estado'),
    path('reservar/<str:patenteVehiculo>/', views.reservar, name='reservar'),
    path('boleta/<int:reserva_id>/', views.boleta, name='boleta'),
    path('crear/', views.crear, name="crear"), 
    path('modificar/<id>/', views.modificar, name="modificar"),
    path('eliminar/<id>/', views.eliminar, name="eliminar"),
    ###################################################################
    path('catalogo_empresas/', views.catalogo_empresas, name='catalogo_empresas'),
    path('crear_empresa/', views.crear_empresa, name='crear_empresa'),
    path('eliminar_empresa/<int:idEmpresa>/', views.eliminar_empresa, name='eliminar_empresa'),
    ###################################################################
    path('catalogo_choferes/', views.catalogo_choferes, name='catalogo_choferes'),
    path('crear_chofer/', views.crear_chofer, name='crear_chofer'),
    path('eliminar_chofer/<int:rutChofer>/', views.eliminar_chofer, name='eliminar_chofer'),
    path('opciones_admin/', views.opciones_admin, name="opciones_admin"), 
    ###################################################################
    path('login/', views.login, name="login"),
    path('logout/', views.cerrar, name='cerrar'),
    
    

]
