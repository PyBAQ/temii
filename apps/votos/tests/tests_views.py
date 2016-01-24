from django.contrib.auth.models import User
from test_plus.test import TestCase

class ViewsTestCase(TestCase):
    
    def setUp(self):
        self.user = User.objects.create_user('testuser', 'lennon@thebeatles.com', 'testpass')

    def test_index_eventos(self):
        self.get('index')
        self.response_200()

    def test_menu_eventos(self):
        self.get('menu')
        self.response_200()

    def test_agendados_eventos(self):
        self.get('charlas/agendadas')
        self.response_200()

    def test_finalizados_eventos(self):
        self.get('charlas/finalizadas')
        self.response_200()

    def test_posibles_eventos(self):
        self.get('charlas/posibles')
        self.response_200()
        
    
    def test_postular_eventos(self):
        user1 = self.make_user('u1')
        user2 = self.make_user('u2')
        self.assertLoginRequired('charlas/postular')
        with self.login(username=user1.username, password='password'):
            response = self.get('charlas/postular')
        self.response_200()