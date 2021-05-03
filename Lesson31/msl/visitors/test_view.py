from django.test import TestCase, Client

class TestVisitorListView(TestCase):

    def test_context_true(self):
        client = Client()
        response = self.client.get('/')
        self.assertIn('org_name', response.context)


    def test_index_context_name(self):
        client = Client()
        response = self.client.get('/')
        self.assertEqual(response.context['org_name'], 'Детский центр "Тропикано"')


    def test_index_status_code(self):
        client = Client()
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_index_content(self):
        client = Client()
        response = self.client.get('/')
        self.assertIn('Добро пожаловать', response.content.decode(encoding='utf-8'))