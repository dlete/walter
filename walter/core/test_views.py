# Core Django imports
from django.test import TestCase
from django.urls import reverse


class CoreViewsTests(TestCase):

    def test_core_about(self):
        '''
        Test the view "about" of the core app.
        '''
        response = self.client.get(reverse('core:about'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "This project is named")
