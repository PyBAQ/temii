from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Voto, Charla
from .forms import RegistrarCharlaForm


class IndexView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.posibles.all()
    template_name = 'index.html'


class ListarEstadoView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.posibles.all()
    template_name = 'listar_estado.html'
    titulo = 'Posibles temas'   
    
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListarEstadoView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['titulo'] = self.titulo
        return context


class ListarAgendadoView(ListarEstadoView):
    queryset = Charla.agendadas.all()
    titulo = 'Temas Agendados'


class ListarFinalizadoView(ListarEstadoView):
    queryset = Charla.finalizadas.all()
    titulo = 'Temas Finalizados'


class RegistrarCharlaView(CreateView):
    form_class = RegistrarCharlaForm
    model = Charla
    success_url = reverse_lazy('index')
    template_name = 'registrar_charla.html'

    def get_form_kwargs(self):
        if self.request.method in ('POST', 'PUT'):
            self.object = self.model()
            self.object.usuario = self.request.user
        kwargs = super(RegistrarCharlaView, self).get_form_kwargs()
        return kwargs