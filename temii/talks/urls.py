from django.urls import path
from django.views.generic import TemplateView

from .views import talk_create_view

app_name = "talks"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/about.html"), name="talks"),
    path("~create/", view=talk_create_view, name="create"),
    path("thanks/", TemplateView.as_view(template_name="talks/talk_thanks.html"), name="thanks"),
]
