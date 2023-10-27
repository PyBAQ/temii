from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from .forms import NewTalkForm
from .models import Talk


class TalkCreateView(LoginRequiredMixin, CreateView):
    """Propose a new talk."""

    model = Talk
    form_class = NewTalkForm
    success_url = reverse_lazy("talks:thanks")

    def form_valid(self, form):
        # Se agrega el usuario que hace la petición al formulario
        form.instance.user = self.request.user
        return super().form_valid(form)


talk_create_view = TalkCreateView.as_view()
