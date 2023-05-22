from django.db import models


# Create your models here.

class EstadoBono(models.Model):
    id_estado_bono = models.AutoField(primary_key=True)
    nombre_estado_bono = models.CharField()


class TipoBono(models.Model):
    id_tipo_bono = models.AutoField(primary_key=True)
    nombre_tipo_bono = models.CharField()


class CategoriaBono(models.Model):
    id_categoria_bono = models.AutoField(primary_key=True)
    nombre_categoria_bono = models.CharField()


class Bono(models.Model):
    id_bono = models.AutoField(primary_key=True)
    id_condominio = models.CharField()
    id_tipo_bono = models.CharField()
    id_modelo = models.CharField()
    id_categoria_bono = models.CharField()
    id_estado_bono = models.CharField()
    nombre_bono = models.CharField()
    desde_bono = models.CharField()
    hasta_bono = models.CharField()
    monto_bono = models.CharField()
    fecha_desde_bono = models.DateField()
    fecha_hasta_bono = models.DateField()
