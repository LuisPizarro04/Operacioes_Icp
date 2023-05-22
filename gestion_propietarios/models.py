from django.db import models


# Create your models here.


class EstadoPropietario(models.Model):
    id_estado_propietario = models.AutoField(primary_key=True)
    nombre_estado_propietario = models.CharField()


class Profesion(models.Model):
    id_profesion = models.AutoField(primary_key=True)
    nombre_profesion = models.CharField()


class Propietario(models.Model):
    id_propietario = models.AutoField(primary_key=True)
    id_nacionalidad = models.CharField()
    id_region = models.CharField()
    id_genero = models.CharField()
    id_estado_civil = models.CharField()
    id_profesion = models.CharField()
    id_estado_propietario = models.CharField()
    rut_propietario = models.CharField()
    pasaporte_propietario = models.CharField()
    nombre_1 = models.CharField()
    nombre_2 = models.CharField()
    apellido_p_propietario = models.CharField()
    apellido_m_propietario = models.CharField()
    fono_propietario = models.CharField()
    fono_2_propietario = models.CharField()
    correo_propietario = models.CharField()
    correo_2_propietario = models.CharField()
    direccion_propietario = models.CharField()
    correo_trabajo_propietario = models.CharField()
    fecha_nac_propietario = models.DateField()
    id_comuna = models.CharField()
    cantidad_seguimiento_propietario = models.CharField()
    fecha_seguimiento_propietario = models.DateField()
    cantidad_observaciones = models.CharField()
    fecha_observacion_propietario = models.CharField()
    profesion_promesa_propietario = models.CharField()

