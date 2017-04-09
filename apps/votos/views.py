from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from . import constants
from .models import Voto, Charla
from .forms import RegistrarCharlaForm

from django.db.models import Q

class LoginRequired(object):
    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(LoginRequired, self).dispatch(*args, **kwargs)


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


class ListarFinalizadoView(ListView):
    context_object_name = 'charlas'
    queryset = Charla.finalizadas.all()
    template_name = 'charla/index.html'


class RegistrarCharlaView(LoginRequired, CreateView):
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


def login(request):
    if not request.user.is_authenticated():
        return render(request, 'login.html')
    else:
        return redirect('/', name='index')


class DetalleCharlaView(DetailView):
    context_object_name = 'charla'
    model = Charla
    template_name = 'charla/detalle.html'

    """A base view for displaying a single object."""
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        try:
            charla = Charla.objects.get(id=self.object.id)
        except:
            return JsonResponse({"html": "Esta Charla no existe" })

        try:
            voto_charla = Voto.objects.get(usuario=request.user, charla=charla)
            estado_estrella = True
        except:
            estado_estrella = False

        context = self.get_context_data(object=self.object)
        context["estado_estrella"] = estado_estrella
        return self.render_to_response(context)


class VotoView(LoginRequired, TemplateView):

    template_name = "charla/voto.html"
    http_method_names = ["post"]

    def post(self, request, *args, **kwargs):
        id = self.kwargs.get("charla", None)
        estado_estrella = True
        try:
            charla = Charla.objects.get(id=id)
        except:
            return JsonResponse({"html": "Esta Charla no existe" })

        if charla.estado == constants.ESTADO_POSIBLE:
            voto, created = Voto.objects.get_or_create(charla=charla,
                                                       usuario=request.user)
            i = 1
            if not created:
                i *= -1
                voto.delete()
                estado_estrella = False


            charla.votos += i
            charla.save()
        response = self.render_to_response({"charla":charla, "estado_estrella": estado_estrella})
        return JsonResponse({"html": response.rendered_content })