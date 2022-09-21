from urllib import response
from django.test import TestCase, Client
from django.urls import resolve #dari slide

class Test(TestCase): #parameter TestCase untuk memanggil python manage.py test
    def test_url_html(self):
        response = Client().get('/mywatchlist/html/')
        self.assertEqual(response.status_code,200)
    def test_url_xml(self):
        response = Client().get('/mywatchlist/xml/')
        self.assertEqual(response.status_code,200)
    def test_url_json(self):
        response = Client().get('/mywatchlist/json/')
        self.assertEqual(response.status_code,200)
