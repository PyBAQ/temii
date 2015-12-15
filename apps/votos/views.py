from django.shortcuts import render
from django.views.generic import ListView

from .models import Voto, Charla

class ListarEstadoView(ListView):
	model = Charla
	template_name = 'index.html'
	estado = 'posible'
	context_object_name = 'charlas'

	def get_queryset(self):
	    queryset = super(ListarEstadoView, self).get_queryset()
	    return queryset.filter(estado = self.estado)


class ListarAgendadoView(ListarEstadoView):
	estado = 'agendado'

class ListarFinalizadoView(ListarEstadoView):
	estado = 'finalizado'