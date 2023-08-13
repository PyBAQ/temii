from django.urls import path
from django.views.generic import TemplateView

app_name = "talks"
urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/about.html"), name="talks"),
]
