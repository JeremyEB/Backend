from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ClientesSerializers
from .serializers import FacturasSerializers
from .serializers import HistorialFacturasSerializers
from .models import Cliente
from .models import Factura
from .models import HistorialFactura

# Create your views here.

#All
@api_view(['GET'])
def ShowAllCliente(request):
    clientes = Cliente.objects.all()
    serializers = ClientesSerializers(clientes, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ShowAllFactura(request):
    facturas = Factura.objects.all()
    serializers = FacturasSerializers(facturas, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ShowAllHistorialFactura(request):
    historialFactura = HistorialFactura.objects.all()
    serializers = FacturasSerializers(historialFactura, many=True)
    return Response(serializers.data)

#Details
@api_view(['GET'])
def ViewCliente(request, identificacion):
    clientes = Cliente.objects.filter(CEDULA=identificacion)
    serializers = ClientesSerializers(clientes, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewFactura(request, pk):
    facturas = Factura.objects.filter(ID_FACTURAS=pk)
    serializers = FacturasSerializers(facturas, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewFacturaCedula(request, identificacion):
    facturas = Factura.objects.filter(CEDULA=identificacion)
    serializers = FacturasSerializers(facturas, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewHistorialFactura(request, pk):
    historialFactura = HistorialFactura.objects.filter(ID_HISTORIALFACTURA=pk)
    serializers = HistorialFacturasSerializers(historialFactura, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewHistorialFacturaCedula(request, identificacion):
    historialFactura = HistorialFactura.objects.filter(CEDULA=identificacion)
    serializers = HistorialFacturasSerializers(historialFactura, many=True)
    return Response(serializers.data)

@api_view(['GET'])
def ViewClientesFecha(request, fecha):
    fechaCliente = Factura.objects.filter(FECHA=fecha)
    serializers = FacturasSerializers(fechaCliente, many=True)
    return Response(serializers.data)

#Create
@api_view(['POST'])
def CreateCliente(request):
    serializers = ClientesSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def CreateFactura(request):
    serializers = FacturasSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['POST'])
def CreateHistorialFactura(request):
    serializers = HistorialFacturasSerializers(data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

#Update
@api_view(['PUT'])
def UpdateClientes(request, pk):
    cliente = Cliente.objects.get(ID_CLIENTE=pk)
    serializers = ClientesSerializers(instance=cliente, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['PUT'])
def UpdateFacturas(request, pk):
    facturas = Factura.objects.get(ID_FACTURAS=pk)
    serializers = FacturasSerializers(instance=facturas, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)

@api_view(['PUT'])
def UpdateHistorialFacturas(request, pk):
    historialFacturas = HistorialFactura.objects.get(ID_HISTORIALFACTURA=pk)
    serializers = historialFacturas(instance=historialFacturas, data=request.data)
    if serializers.is_valid():
        serializers.save()
    return Response(serializers.data)


#Delete
@api_view(['GET'])
def DeleteClientes(request, pk):
    cliente = Cliente.objects.get(ID_CLIENTE=pk)
    cliente.delete()
    return Response('Cliente eliminado satisfactoriamente')

@api_view(['GET'])
def DeleteFacturas(request, pk):
    factura = Factura.objects.get(ID_FACTURAS=pk)
    factura.delete()
    return Response('Factura eliminada satisfactoriamente')

def DeleteHistorialFacturas(request, pk):
    historialFactura = HistorialFactura.objects.get(ID_HISTORIALFACTURA=pk)
    historialFactura.delete()
    return Response('Factura del historial eliminado satisfactoriamente')