from django.db import models

# Create your models here.

class Cliente(models.Model):
    ID_CLIENTE = models.AutoField(primary_key=True, null=False)
    NOMBRE_APELLIDO = models.CharField(max_length=150, null=False)
    TELEFONO = models.CharField(max_length=15, null=False)
    CEDULA = models.CharField(max_length=20, null=False)


class Factura(models.Model):
    ID_FACTURAS = models.AutoField(primary_key = True, null=False)
    MONTO_SOLICITADO = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    TASA = models.DecimalField(max_digits=5, null=False, decimal_places=2)
    CUOTAS = models.DecimalField(max_digits=5, null=False, decimal_places=2)
    CUOTAS_MENSUALES = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    CAPITAL = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    INTERES = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    PAGO_NUEVO = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    PAGO_REALIZADO = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    FECHA = models.DateField()
    CLIENTE_ID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    NOMBRE_APELLIDO = models.CharField(max_length=150, null=False)
    TELEFONO = models.CharField(max_length=15, null=False)
    CEDULA = models.CharField(max_length=20, null=False)

class HistorialFactura(models.Model):
    ID_HISTORIALFACTURA = models.AutoField(primary_key = True, null=False)
    MONTO_SOLICITADO = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    TASA = models.DecimalField(max_digits=5, null=False, decimal_places=2)
    CUOTAS = models.DecimalField(max_digits=5, null=False, decimal_places=2)
    CUOTAS_MENSUALES = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    CAPITAL = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    INTERES = models.DecimalField(max_digits=10, null=False, decimal_places=2)
    PAGO_NUEVO = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    PAGO_REALIZADO = models.DecimalField(max_digits=10, null=True, decimal_places=2)
    FECHA = models.DateField()
    FACTURA_ID = models.ForeignKey(Factura, on_delete=models.CASCADE)
    CLIENTE_ID = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    NOMBRE_APELLIDO = models.CharField(max_length=150, null=False)
    TELEFONO = models.CharField(max_length=15, null=False)
    CEDULA = models.CharField(max_length=20, null=False)