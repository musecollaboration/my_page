from django.test import TestCase
from django.urls import reverse
from . import views


class TestHoroscope(TestCase):

    def test_index(self):
        response = self.client.get('/horoscope/')
        self.assertEqual(response.status_code, 200)

    def test_libra(self):
        response = self.client.get('/horoscope/libra/')
        self.assertEqual(response.status_code, 200)
        pattern = 'Весы - седьмой знак зодиака. Рожден 24 сентября - 23 октября'
        self.assertIn(pattern, response.content.decode())

    def test_libra_redirect(self):
        for num, sign in enumerate(views.dict_zodiac, 1):
            redirect_url = reverse('horoscope-num', args=[num])
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(response.url, reverse('horoscope-name', args=[sign]))

    def test_signs(self):
        for sign in views.dict_zodiac:
            redirect_url = reverse('horoscope-name', args=[sign])
            response = self.client.get(redirect_url)
            self.assertEqual(response.status_code, 200)
            pattern = views.dict_zodiac[sign]
            self.assertIn(pattern, response.content.decode())
