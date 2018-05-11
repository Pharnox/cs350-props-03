# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from geopy.distance import distance
from geopy.geocoders import Nominatim

from .models import Property

from .forms import LookupForm
from .forms import DistanceForm


# Show the all the properties in the db.

class PropertyListView(generic.ListView):
    model = Property
    template_name = "properties/list.html"


class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = "properties/detail.html"


class PropertyCreateView(generic.CreateView):
    model = Property  # what type of object we are creating?
    template_name = "properties/create.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')


class PropertyUpdateView(generic.UpdateView):
    model = Property  # what type of object we are editing?
    template_name = "properties/edit.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')
    
class LookupView(generic.FormView):
    template_name = "properties/lookup.html"
    form_class = LookupForm
    success_url = reverse_lazy('properties:lookup')
    
    def get_context_data(self, **kwargs):
        context = super(LookupView, self).get_context_data(**kwargs)
        
        try:        
            q = self.request.GET['search']
            properties = Property.objects.all()
            results = []
            for i in properties:
                if q in i.prop_type:
                    results.append(i)
            
            context['results'] = results
            context['report'] = True 
        except Exception as e:
            pass
        return context
        
class DistanceView(generic.FormView):
    template_name = "properties/distance.html"
    form_class = DistanceForm
    success_url = reverse_lazy('properties:distance')
    
    def get_context_data(self, **kwargs):
        context = super(DistanceView, self).get_context_data(**kwargs)
        
        try:        
            adder = self.request.GET['address']
            dist = int(self.request.GET['distance'])
            geolocator = Nominatim()
            loc = geolocator.geocode(adder)
            results = []
            if not loc:
                context['results'] = 'Location not found in Nominatim'
            else:
                properties = Property.objects.all()
                for i in properties:
                    target = geolocator.geocode(i.address)
                    d = distance((loc.latitude, loc.longitude), (target.latitude, target.longitude)).miles
                    if d < dist:
                        results.append(i)
                print(results)
                context['results'] = results
        except Exception as e:
            print(e)
        return context