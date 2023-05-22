from django.db import models


# Create your models here.


class CierreMes(models.Model):
    id_cierremes = models.AutoField(primary_key=True)
    id_usuario = models.CharField()
    id_mes = models.CharField()
    agno_cierremes = models.CharField()
    fecha_desde_cierremes = models.CharField()
    fecha_hasta_cierremes = models.CharField()


class BonoCierre(models.Model):
    id_bono_cierre = models.AutoField(primary_key=True)
    id_cierremes = models.CharField()
    id_condominio = models.CharField()
    id_usuario = models.CharField()
    nombre_bono_cierremes = models.CharField()
    fecha_desde_bono_cierremes = models.CharField()
    fecha_hasta_bono_cierremes = models.CharField()
    monto_bono_cierremes = models.CharField()

