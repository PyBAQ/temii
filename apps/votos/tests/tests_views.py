from test_plus.test import TestCase

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
