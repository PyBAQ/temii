#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

ESTADO_CHOICES = (
    			   ('posible','Temas Posibles'),
    			   ('agendado','Temas agendados'),
    			   ('finalizado','Temas finalizados'),)


class Categoria(models.Model):
	nombre = models.CharField(max_length=255)

	def __unicode__(self):
		return self.nombre


# Create your models here.
class Charla(models.Model):
	titulo = models.CharField(max_length=255)
	descripcion = models.TextField(blank=True, null=True)
	fecha_publicacion = models.DateTimeField(auto_now_add=True)
	categorias = models.ManyToManyField(Categoria)
	prerequisitos = models.TextField(blank=True, null=True)
	estado = models.CharField(max_length=255, choices=ESTADO_CHOICES, default="posible")	
	fecha_taller = models.DateField(blank=True,null=True)
	votos = models.PositiveIntegerField(default=0)

	class Meta:
		ordering = ['votos']

	def __unicode__(self):
		return self.titulo


class Voto(models.Model):
	usuario = models.ForeignKey(User)
	charla = models.ForeignKey(Charla)
	timestamp = models.DateTimeField(auto_now_add=True)

	class Meta:
		unique_together = ('usuario', 'charla')
