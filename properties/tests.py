# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from django.test import Client
from django.urls import reverse
from django.utils.http import urlencode

# Create your tests here.
class TestPropertyViews(TestCase):
    fixtures = ['property-testdata.json']
    
    def test_LookupView(self):
        client = Client()
        query = urlencode({'search':'House'})
        url = reverse('properties:lookup') + '?' + query
        response = client.get(url)
        result = response.context['results']
        expected_count = 2
        results_count = len(result)
        self.assertEqual(results_count, expected_count)

    def test_DistanceView(self):
        client = Client()
        nmhu = urlencode({'address':'1009 Diamond St, Las Vegas, NM'})
        distance = urlencode({'distance':'100'})
        url = reverse('properties:distance') + '?' + nmhu + '&' + distance
        response = client.get(url)
        result = response.context['results']
        expected_count = 2
        results_count = len(result)
        self.assertEqual(results_count, expected_count)