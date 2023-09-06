from django.db import models
from django.utils.translation import gettext_lazy as _

from temii.users.models import User


class Talk(models.Model):
    class Level(models.IntegerChoices):
        BEGINNER = 1, _("Beginner")
        INTERMEDIATE = 2, _("Intermediate")
        ADVANCED = 3, _("Advanced")

    class Language(models.TextChoices):
        ES = "es", _("Spanish")
        EN = "en", _("English")

    user = models.ForeignKey(User, on_delete=models.PROTECT)
    name = models.CharField(_("Name"), max_length=60)
    description = models.CharField(_("Description"), max_length=300)
    level = models.PositiveIntegerField(_("Level"), choices=Level.choices, default=Level.BEGINNER)
    language = models.CharField(_("Language"), max_length=2, choices=Language.choices, default=Language.ES)
    timezone = models.CharField(_("Timezone"), max_length=60)
    comments = models.CharField(_("Comments"), max_length=300)

    class Meta:
        verbose_name = _("Talk")
