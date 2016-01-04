from django.shortcuts import render
from django.views.generic import ListView

from .models import Voto, Charla


class ListarEstadoView(ListView):
	context_object_name = 'charlas'
	queryset = Charla.posibles.all()
	template_name = 'index.html'


class ListarAgendadoView(ListarEstadoView):
	queryset = Charla.agendadas.all()


class ListarFinalizadoView(ListarEstadoView):
	queryset = Charla.finalizadas.all()
