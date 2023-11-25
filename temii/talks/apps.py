from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class TalksConfig(AppConfig):
    name = "temii.talks"
    verbose_name = _("Talks")
    default_auto_field = "django.db.models.BigAutoField"
