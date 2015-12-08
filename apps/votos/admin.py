from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Categoria)
class CategoriaAdmin(admin.ModelAdmin):
	list_display = ['id', 'nombre']


@admin.register(models.Charla)
class CharlaAdmin(admin.ModelAdmin):
	list_display = [
		'id', 'titulo', 'fecha_publicacion', 'estado',
		'fecha_taller', 'votos'
	]
	search_fields = ['titulo']
	list_filter = ['estado', 'fecha_taller']


@admin.register(models.Voto)
class VotoAdmin(admin.ModelAdmin):
	list_display = ['id', 'usuario', 'charla']
	list_filter = ['usuario']
