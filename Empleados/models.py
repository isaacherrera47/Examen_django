# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models

# Create your models here.

class Empleado(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    direccion = models.CharField(max_length=255)
    area = models.CharField(max_length=200)
    comentarios = models.CharField(max_length=200)
    fecha_nacimiento = models.DateField('Fecha de nacimiento')

class Etiquetas(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete= models.CASCADE)
    etiqueta = models.CharField(max_length=30)