from django.db import models


# Create your models here.


class EstadoDescuento(models.Model):
    id_estado_descuento = models.AutoField(primary_key=True)
    nombre_estado_descuento = models.CharField()


class Descuento(models.Model):
    id_descuento = models.AutoField(primary_key=True)
    id_condominio = models.CharField()
    id_estado_descuento = models.CharField()
    nombre_descuento = models.CharField()
    monto_descuento = models.CharField()
