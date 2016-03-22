import factory

from .. import models

from .user import UserFactory


class CharlaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = models.Charla

    titulo = factory.Sequence(lambda n: "Charla #{0}".format(str(n)))
    usuario = factory.SubFactory(UserFactory)
