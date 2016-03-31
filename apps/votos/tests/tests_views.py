# -*- coding: utf-8 -*-

import unittest

from test_plus.test import TestCase

from ..factories.user import UserFactory
from ..factories.charla import CharlaFactory

from .. import constants
from ..models import Charla


class ViewsTestCase(TestCase):

    def setUp(self):
        self.user = UserFactory()

    def test_index_eventos(self):
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

    def test_user_name_in_index(self):
        with self.login(username=self.user.username, password='1234'):
            response = self.get("index")
            self.assertContains(response,
                                '<span class="truncate">¡Hola! @{}</span>'.format(self.user.username),
                                status_code=200)


class TestCharlaView(TestCase):

    def test_charlas_posibles(self):
        CharlaFactory(estado=constants.ESTAOO_FINALIZADO)
        qs = [CharlaFactory(estado=constants.ESTADO_POSIBLE)]
        self.get('index')
        charlas = self.get_context('charlas')
        self.assertEqual(len(qs), charlas.count())
        for i,model in enumerate(charlas):
            self.assertEqual(qs[i], model)

    def test_charlas_seleccionadas(self):
        CharlaFactory(estado=constants.ESTAOO_FINALIZADO)
        qs = [CharlaFactory(estado=constants.ESTADO_AGENDADO),
              CharlaFactory(estado=constants.ESTADO_POSIBLE)]
        self.get('index')
        charlas = self.get_context('charlas')
        self.assertEqual(len(qs), charlas.count())
        for i,model in enumerate(charlas):
            self.assertEqual(qs[i], model)

    def test_charlas_agendadas(self):
        CharlaFactory(estado=constants.ESTAOO_FINALIZADO)
        CharlaFactory(estado=constants.ESTADO_POSIBLE)
        qs = [CharlaFactory(estado=constants.ESTADO_AGENDADO)]
        self.get('agendado')
        charlas = self.get_context('charlas')
        self.assertEqual(len(qs), charlas.count())
        for i,model in enumerate(charlas):
            self.assertEqual(qs[i], model)

    def test_charlas_finalizadas(self):
        CharlaFactory(estado=constants.ESTADO_AGENDADO)
        CharlaFactory(estado=constants.ESTADO_POSIBLE)
        qs = [CharlaFactory(estado=constants.ESTAOO_FINALIZADO)]
        self.get('finalizado')
        charlas = self.get_context('charlas')
        self.assertEqual(len(qs), charlas.count())
        for i,model in enumerate(charlas):
            self.assertEqual(qs[i], model)


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
