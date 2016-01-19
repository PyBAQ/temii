from django.test import TestCase

from .. import models

class TestModels(TestCase):

    def test_create_category(self):
        category = models.Categoria(nombre="test")
        category.save()
        self.assertEqual(1, models.Categoria.objects.count())

    def test_str_category(self):
        category = models.Categoria(nombre="test")
        category.save()
        self.assertEqual("test", str(category))


class CharlaModelTest(TestCase):

    def setUp(self):
        self.testUser = models.User.objects.create(username='testUser1')

    def test_default_titulo(self):
        charla = models.Charla()
        self.assertEqual(charla.titulo, '')

    def test_charla_tiene_asociada_una_categoria(self):
        categoria_ = models.Categoria.objects.create()
        categoria_.nombre = 'TestCategoria'
        categoria_.save()

        charla = models.Charla()
        charla.usuario = self.testUser
        charla.titulo = 'CharlaTest'
        charla.save()

        charla.categorias.add(categoria_)
        self.assertEqual(charla.categorias.get(pk=categoria_.pk), categoria_)
