from django.urls import path
from . import views

urlpatterns = [
    #Listas
    path('clientes_list', views.ShowAllCliente, name='clientes-list'),
    path('facturas_list', views.ShowAllFactura, name='facturas-list'),
    path('historialFactura_list', views.ShowAllHistorialFactura, name='historialFacturas-list'),
    #Detalles
    path('clientes_detalles/<str:identificacion>', views.ViewCliente, name='clientes-details'),
    path('facturas_detalles/<int:pk>', views.ViewFactura, name='facturas-details'),
    path('facturas_detalles_cedula/<str:identificacion>', views.ViewFacturaCedula, name='facturas-details-cedula'),
    path('historialFacturas_detalles/<int:pk>', views.ViewHistorialFactura, name='historial-details'),
    path('historialFacturas_detalles_cedula/<str:identificacion>', views.ViewHistorialFacturaCedula, name='historial-details-cedula'),
    path('fechaClientes/<str:fecha>', views.ViewClientesFecha, name='fechaClientes-list'),
    #Creando
    path('creando_clientes', views.CreateCliente, name='clientes-create'),
    path('creando_facturas', views.CreateFactura, name='facturas-create'),
    path('creando_historialFactura', views.CreateHistorialFactura, name='historial-create'),
    #Actualizar
    path('actualizando_clientes/<int:pk>', views.UpdateClientes, name='clientes-update'),
    path('actualizando_facturas/<int:pk>', views.UpdateFacturas, name='facturas-update'),
    path('actualizando_historialFactura/<int:pk>', views.UpdateHistorialFacturas, name='historial-update'),
    #Delete
    path('borrar_clientes/<int:pk>', views.DeleteClientes, name='clientes-delete'),
    path('borrar_facturas/<int:pk>', views.DeleteFacturas, name='facturas-delete'),
    path('borrar_historialFactura/<int:pk>', views.DeleteHistorialFacturas, name='historial-delete'),
]