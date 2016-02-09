# -*- coding: utf-8 -*-

import unittest

from test_plus.test import TestCase

from ..factories.user import UserFactory


class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

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
        with self.login(username=self.user.username, password='1234'):
            response = self.post('registrar_charla',
                                 data={"titulo": "charla 1",
                                       "descripcion": "descripcion 1"})
            self.response_200(response)

    @unittest.expectedFailure
    def test_fail_post_registrar_charla(self):
        with self.login(username=self.user.username, password='1234'):
            response = self.post('registrar_charla',
                                 data={"titulo": "charla 1"})
            self.response_200(response)

    def test_user_name_in_index(self):
        with self.login(username=self.user.username, password='1234'):
            response = self.get("index")
            self.assertContains(response,
                                '<span class="truncate">¡Hola! @{}</span>'.format(self.user.username),
                                status_code=200)


class ViewTemplateTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_index_template(self):
        response = self.get("index")
        self.assertTemplateUsed(response,"charla/index.html")

    def test_get_registrar_charla(self):
        with self.login(username=self.user.username, password='1234'):
            response = self.get('registrar_charla')
            self.assertTemplateUsed(response, "charla/registrar.html")
