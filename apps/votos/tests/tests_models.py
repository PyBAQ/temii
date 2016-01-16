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


        