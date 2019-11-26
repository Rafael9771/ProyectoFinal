from django.db import models

import sys
sys.path.append("..")
from Administracion.models import *

class login(models.Model):
    id_login = models.AutoField(primary_key=True)
    nombre = models.CharField('nombre', blank=False, max_length=20)
    apellido_paterno = models.CharField('apellido_paterno', blank=False, max_length=15)
    apellido_materno = models.CharField('apellido_materno', blank=True, max_length=15)
    email = models.EmailField
    username = models.CharField('username', blank=False, max_length=20)
    password = models.CharField('password', blank=False, max_length=20)
    saldo = models.IntegerField('saldo', blank=False, default=0)
    fecha_creacion = models.DateField(default=datetime.date.today)
    fecha_modificacion = models.DateField(default=datetime.date.today)
    status = models.CharField('status', blank=True, max_length=1, default='B')

    class Meta:
        db_table = 'login'


class favoritos(models.Model):
    id_favorito = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'favoritos'


class compra(models.Model):
    id_compra = models.AutoField(primary_key=True)
    libro = models.ForeignKey(Libro, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'compra'


class compraR(models.Model):
    id_compra = models.AutoField(primary_key=True)
    revista = models.ForeignKey(Revista, blank=False, on_delete=models.CASCADE)
    login = models.ForeignKey(login, blank=False, on_delete=models.CASCADE)

    class Meta:
        db_table = 'compraR'


class comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    texto = models.CharField('texto', blank=False, max_length=1000)
    login = models.ForeignKey(login, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)

    class Meta:
        db_table = 'comentario'
