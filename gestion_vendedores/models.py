from django.db import models


# Create your models here.


class EstadoVendedor(models.Model):
    id_estadovendedor = models.AutoField(primary_key=True)
    nombre_estadovendedor = models.CharField


class CategoriaVendedor(models.Model):
    id_categoriavendedor = models.AutoField(primary_key=True)
    nombre_categoriavendedor = models.CharField


class Vendedor(models.Model):
    id_vendedor = models.AutoField(primary_key=True)
    id_categoria_vendedor = models.CharField()
    id_usuario = models.CharField()
    id_estado_vendedor = models.CharField()
    rut_vendedor = models.CharField()
    nombre_vendedor = models.CharField()
    apellido_p_vendedor = models.CharField()
    apellido_m_vendedor = models.CharField()
    correo_vendedor = models.EmailField()
    fono_vendedor = models.CharField()


class SupervisorVendedor(models.Model):
    id_supervisorvendedor = models.AutoField(primary_key=True)
    id_vendedor = models.CharField()
    id_usuario = models.CharField()


class JefeVendedor(models.Model):
    id_jefevendedor = models.AutoField(primary_key=True)
    id_vendedor = models.CharField()
    id_usuario = models.CharField()