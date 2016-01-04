from django.db import models

from .. import constants

class CharlaManager(models.Manager):

    _estado = None

    def get_queryset(self):
        return super(CharlaManager, self).get_queryset().filter(estado=self._estado)


class CharlaPosibleManager(CharlaManager):
    _estado = constants.ESTADO_POSIBLE

class CharlaAgendadaManager(CharlaManager):
    _estado = constants.ESTADO_AGENDADO


class CharlaFinalizadaManager(CharlaManager):
    _estado = constants.ESTAOO_FINALIZADO
