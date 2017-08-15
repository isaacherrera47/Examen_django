"""Examen URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Empleados import views as empleados_views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^nuevo_empleado/$', empleados_views.nuevo_empleado, name="nuevo_empleado"),
    url(r'^guardar/$', empleados_views.guardar_empleado, name="guardar_empleado"),
    url(r'^$', empleados_views.index, name="index"),
]
