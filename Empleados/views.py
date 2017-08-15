# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from models import Empleado, Etiquetas
# Create your views here.
def index(request):
    empleados = Empleado.objects.all()
    context = {
        'empleados' : empleados
    }
    return render(request, "Empleados/index.html", context)

def nuevo_empleado(request):
    return render(request, "Empleados/nuevo_empleado.html")

def guardar_empleado(request):
    nombre = request.POST['nombre']
    apellidos = request.POST['apellidos']
    fecha_nacimiento = request.POST['fecha_nacimiento']
    email = request.POST['email']
    area = request.POST['puesto']
    direccion = request.POST['direccion']
    comentarios = request.POST['comentarios']
    user = User.objects.create_user(email,email,'UdxSsdFDE2') # ToDo: generate passwords
    user.first_name = nombre
    user.last_name = apellidos
    user.is_active = True
    user.save()

    empleado = Empleado.objects.create(fecha_nacimiento= fecha_nacimiento, area= area, user = user, direccion = direccion, comentarios= comentarios)
    empleado.save()
    return HttpResponseRedirect(reverse('index'))