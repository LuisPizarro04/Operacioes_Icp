from django.db import models


# Create your models here.


class EstadoModelo(models.Model):
    id_estado_modelo = models.AutoField(primary_key=True)
    nombre_estado_modelo = models.CharField()


class EstadoVivienda(models.Model):
    id_estado_vivienda = models.AutoField(primary_key=True)
    nombre_estado_vivienda = models.CharField()


class EstadoTorre(models.Model):
    id_estado_torre = models.AutoField(primary_key=True)
    nombre_estado_torre = models.CharField()


class EstadoEstacionamiento(models.Model):
    id_estado_estacionamiento = models.AutoField(primary_key=True)
    nombre_estado_estacionamiento = models.CharField()


class TipoVivienda(models.Model):
    id_tipo_vivienda = models.AutoField(primary_key=True)
    nombre_tipo_vivienda = models.CharField()


class EstadoCondominio(models.Model):
    id_estado_condominio = models.AutoField(primary_key=True)
    nombre_estado_condominio = models.CharField()


class EstadoBodega(models.Model):
    id_estado_bodega = models.AutoField(primary_key=True)
    nombre_estado_bodega = models.CharField()


class OrientacionVivienda(models.Model):
    id_orientacion_vivienda = models.AutoField(primary_key=True)
    nombre_orientacion_vivienda = models.CharField()


class Modelo(models.Model):
    id_modelo = models.AutoField(primary_key=True)
    id_estado_modelo = models.CharField()
    nombre_modelo = models.CharField()
    numero_cama_modelo = models.CharField()
    numero_bagno_modelo = models.CharField()
    descripcion_modelo = models.TextField()


class Torre(models.Model):
    id_torre = models.AutoField(primary_key=True)
    id_condominio = models.CharField()
    id_estado_torre = models.CharField()
    nombre_torre = models.CharField()


class Piso(models.Model):
    id_piso = models.AutoField(primary_key=True)
    nombre_piso = models.CharField()


class Vivienda(models.Model):
    id_vivienda = models.AutoField(primary_key=True)
    id_tipo_vivienda = models.CharField()
    id_torre = models.CharField()
    id_modelo = models.CharField()
    id_ori_vivienda = models.CharField()
    id_estado_vivienda = models.CharField()
    id_piso_vivienda = models.CharField()
    nombre_vivienda = models.CharField()
    valor_vivienda = models.CharField()
    metros_vivienda = models.CharField()
    metros_terraza_vivienda = models.CharField()
    metros_total_vivienda = models.CharField()
    bono_vivienda = models.CharField()
    prorrateo_vivienda = models.CharField()
    rol_vivienda = models.CharField()


class Estacionamiento(models.Model):
    id_estacionamiento = models.AutoField(primary_key=True)
    id_condominio = models.CharField()
    id_vivienda = models.CharField()
    id_estado_estacionamiento = models.CharField()
    nombre_estacionamiento = models.CharField()
    valor_estacionamiento = models.CharField()


class Condominio(models.Model):
    id_condominio = models.AutoField(primary_key=True)
    id_estado_condominio = models.CharField()
    nombre_condominio = models.CharField()
    alias_condominio = models.CharField()
    fecha_venta_condominio = models.DateField()


class DocumentoCondominio(models.Model):
    id_documentocondominio = models.AutoField(primary_key=True)
    id_condominio = models.AutoField(primary_key=True)
    nombre_documentocondominio = models.CharField()


class Bodega(models.Model):
    id_bodega = models.AutoField(primary_key=True)
    id_condominio = models.CharField()
    id_vivienda = models.CharField()
    id_estado_bodega = models.CharField()
    nombre_bodega = models.CharField()
    valor_bodega = models.CharField()
    rol_bodega = models.CharField()
