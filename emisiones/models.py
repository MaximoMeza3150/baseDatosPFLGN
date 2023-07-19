from django.db import models
from django.contrib.auth.models import User


# Create your models here.
SITE_CHOICES = (('PISCO', 'Pisco'), ('MALVINAS', 'Malvinas'))
YACIMIENTO_CHOICES = (('PROCESOS', 'Procesos'), ('SERVICIOS', 'Servicios'))
AREA_CHOICES = (('SERVICIOS AUXILIARES 1 ', 'Servicios auxiliares 1'), ('SERVICIOS AUXILIARES 2', 'Servicios auxiliares 2'))

class Emision(models.Model):
    site = models.CharField(max_length=20, choices=SITE_CHOICES, default='Pisco')
    yacimiento = models.CharField(max_length=100, choices=YACIMIENTO_CHOICES, default='Pisco')
    area = models.CharField(max_length=100)
    sistema = models.CharField(max_length=100)
    ubicacion = models.TextField(max_length=200)
    fuga = models.TextField(max_length=300)
    fluido = models.CharField(max_length=100)
    sustancia = models.CharField(max_length=100)
    componente = models.CharField(max_length=100)
    instalacion = models.CharField(max_length=100)
    tamAccesorio = models.CharField(max_length=100)
    medicion = models.PositiveIntegerField()
    medicion15 = models.CharField(max_length=100)
    presion = models.CharField(max_length=100)
    ciclado = models.CharField(max_length=50)
    ignicion = models.CharField(max_length=50)
    localizacion = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    fechaReporte = models.DateField()
    updated_at = models.DateTimeField(null=True)
    created_at = models.DateField(auto_now_add=True,null=True)
    emisionSuperada = models.BooleanField(default=False)
    FCF = models.PositiveSmallIntegerField(null=True)
    categoria = models.CharField(max_length=10, null=True)
    imagen = models.ImageField(upload_to='images_emisiones', null=True)

    def __str__(self):
        return self.area + ' - ' + self.ubicacion