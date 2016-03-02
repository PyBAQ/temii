from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render_to_response, redirect
from django.views.generic import CreateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.template.context import RequestContext

from . import constants
from .models import Voto, Charla
from .forms import RegistrarCharlaForm

from django.db.models import Q

class ListarEstadoView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.objects.all().order_by("estado")
    template_name = 'charla/index.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super(ListarEstadoView, self).get_queryset(*args, **kwargs)
        queryset = queryset.filter(Q(estado=constants.ESTADO_POSIBLE)|
                                   Q(estado=constants.ESTADO_AGENDADO))
        return queryset



class ListarAgendadoView(ListarEstadoView):
    queryset = Charla.agendadas.all()


class ListarFinalizadoView(ListarEstadoView):
    queryset = Charla.finalizadas.all()


class RegistrarCharlaView(CreateView):
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

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(RegistrarCharlaView, self).dispatch(*args, **kwargs)


def login(request):
    if not request.user.is_authenticated():
        context = RequestContext(request, {
            'request': request, 'user': request.user})
        return render_to_response('login.html', context_instance=context)
    else:
        return redirect('/', name='index')


class DetalleCharlaView(DetailView):
    context_object_name = 'charla'
    model = Charla
    template_name = 'charla/detalle.html'