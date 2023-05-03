from rest_framework import serializers
from .models import Cliente, Factura, HistorialFactura

class ClientesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class FacturasSerializers(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = '__all__'

class HistorialFacturasSerializers(serializers.ModelSerializer):
    class Meta:
        model = HistorialFactura
        fields = '__all__'