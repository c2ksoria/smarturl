from datetime import datetime
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Estado(models.Model):
    NombreEstado=models.CharField(max_length=50, verbose_name='nombre')

    def __str__(self):
        return self.NombreEstado

class Paquete(models.Model):
    estado=models.ForeignKey(Estado, on_delete=models.SET_NULL,null=True,verbose_name='Estado')
    NombrePaquete=models.CharField(max_length=50, blank=False, verbose_name='Nombre')
    CantCampana=models.IntegerField(blank=False, null=False,verbose_name='Cantidad de Capañas')
    CantFoto=models.IntegerField(blank=False, null=False,verbose_name='Cantidad de Fotos', default=0)
    FechaCreacion=models.DateField(auto_now=True, null=True)
    HoraCreacion=models.TimeField(auto_now=True, null=True)

    def __str__(self):
        return self.NombrePaquete

class Empresa(models.Model):
    estado= models.ForeignKey(Estado, on_delete=models.SET_NULL,null=True,verbose_name='Estado')
    Usuario=models.OneToOneField(User,on_delete=models.SET_NULL,null=True,verbose_name='Usuario' )
    NombreEmpresa=models.CharField(max_length=50, blank=True, verbose_name='Nombre')
    DireccionEmpresa=models.CharField(max_length=100, verbose_name='Direccion')
    CuitEmpresa=models.CharField(max_length=11, verbose_name='Cuit')
    FechaIngreso=models.DateField(auto_now=True, null=True)
    HoraIngreso=models.TimeField(auto_now=True, null=True)
    PaqueteContratado=models.ForeignKey(Paquete, on_delete=models.CASCADE, null=False,verbose_name='Paquete')
    Logo= models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.NombreEmpresa


class Campana(models.Model):
    empresa=models.ForeignKey(Empresa, on_delete=models.Case,null=True);
    estado=models.ForeignKey(Estado, on_delete=models.SET_NULL,null=True,verbose_name='Estado')
    NombreCampana=models.CharField(max_length=50, blank=False, verbose_name='Nombre')
    FechaCreacion=models.DateField(auto_now=True, null=True, verbose_name='Fecha Creación')
    HoraCreacion=models.TimeField(auto_now=True, null=True,verbose_name='Hora Creación')
    Temporizado=models.IntegerField(blank=False, null=False,verbose_name='Temporizado de Fotos', default=0)
    url=models.CharField(max_length=100, blank=False, verbose_name='url',help_text="detallar una Url", unique=True)
    
    def __str__(self):
        return self.NombreCampana

class Multimedia(models.Model):
    estado=models.ForeignKey(Estado, on_delete=models.SET_NULL,null=True,verbose_name='Estado')
    NombreMultimedia=models.CharField(max_length=50, blank=False, verbose_name='Nombre Ítem')
    Texto=models.CharField(max_length=50, blank=False, verbose_name='Texto')
    capana=models.ForeignKey(Campana, on_delete=models.CASCADE,null=True,verbose_name='Campana')
    Imagen= models.ImageField(upload_to='campana/', null=True, blank=False)

    def __str__(self):
        return self.Texto
