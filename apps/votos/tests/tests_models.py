from django.test import TestCase

from .. import models

from ..factories import charla

from .. import constants


class TestModels(TestCase):

    def test_create_category(self):
        category = models.Categoria(nombre="test")
        category.save()
        self.assertEqual(1, models.Categoria.objects.count())

    def test_str_category(self):
        category = models.Categoria(nombre="test")
        category.save()
        self.assertEqual("test", str(category))


class TestCharlaModel(TestCase):

    def setUp(self):
        for estado in constants.ESTADO_CHOICES:
            charla.CharlaFactory(estado=estado[0])

    def test_queryset_posible(self):
        self.assertEqual(1, models.Charla.posibles.count())

    def test_queryset_agendado(self):
        self.assertEqual(1, models.Charla.agendadas.count())

    def test_queryset_finalizado(self):
        self.assertEqual(1, models.Charla.finalizadas.count())
