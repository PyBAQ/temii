from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView, ListView

from .models import Voto, Charla
from .forms import RegistrarCharlaForm

class ListarEstadoView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.posibles.all()
    template_name = 'charla/index.html'


class ListarAgendadoView(ListarEstadoView):
    queryset = Charla.agendadas.all()


class ListarFinalizadoView(ListarEstadoView):
    queryset = Charla.finalizadas.all()


class RegistrarCharlaView(LoginRequiredMixin, CreateView):
    form_class = RegistrarCharlaForm
    model = Charla
    success_url = reverse_lazy('index')
    template_name = 'charla/registrar.html'

    def get_form_kwargs(self):
        if self.request.method in ('POST', 'PUT'):
            self.object = self.model()
            self.object.usuario = self.request.user
        kwargs = super(RegistrarCharlaView, self).get_form_kwargs()
        return kwargs


def sing_up(request):
    return render(request, "login.html")
