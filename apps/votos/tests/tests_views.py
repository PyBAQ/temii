import unittest

from test_plus.test import TestCase

from ..factories.user import UserFactory


class ViewsTestCase(TestCase):

    def test_posibles_eventos(self):
        self.get('index')
        self.response_200()

    def test_agendados_eventos(self):
        self.get('agendado')
        self.response_200()

    def test_finalizados_eventos(self):
        self.get('finalizado')
        self.response_200()

    def test_get_registrar_charla(self):
        self.assertLoginRequired('registrar_charla')

    def test_post_registrar_charla(self):
        user = UserFactory()
        with self.login(username=user.username, password='1234'):
            response = self.post('registrar_charla',
                                 data={"titulo": "charla 1",
                                       "descripcion": "descripcion 1"})
            self.response_200(response)
