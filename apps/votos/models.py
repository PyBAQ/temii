# encoding:utf-8
from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import python_2_unicode_compatible

from . import constants

from .managers import charla


@python_2_unicode_compatible
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre


@python_2_unicode_compatible
class Charla(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    categorias = models.ManyToManyField(Categoria)
    prerequisitos = models.TextField(blank=True, null=True)
    estado = models.CharField(max_length=255, choices=constants.ESTADO_CHOICES,
                              default="posible")
    fecha_taller = models.DateField(blank=True, null=True)
    votos = models.PositiveIntegerField(default=0)
    usuario = models.ForeignKey(User, related_name='propone_charla')
    tallerista = models.ForeignKey(User, related_name='tallerista',
                                   blank=True, null=True)

    objects = models.Manager()
    posibles = charla.CharlaPosibleManager()
    agendadas = charla.CharlaAgendadaManager()
    finalizadas = charla.CharlaFinalizadaManager()

    class Meta:
        ordering = ['votos']

    def __str__(self):
        return self.titulo


class Voto(models.Model):
    usuario = models.ForeignKey(User)
    charla = models.ForeignKey(Charla)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('usuario', 'charla')

class Faq(models.Model):
    pregunta = models.CharField(max_length=255)
    respuesta = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre
