# properties/urls.py

from django.conf.urls import url

from . import views

app_name = 'properties'

urlpatterns = [
    url(r'^$', views.PropertyListView.as_view(), name='list'),
    url(r'^add/$', views.PropertyCreateView.as_view(), name='add'),

# http://localhost:8000/property/edit/1/
    url(r'^edit/(?P<pk>[0-9]+)/$', views.PropertyUpdateView.as_view(), name='edit'),

# http://localhost:8000/property/1/
    url(r'^(?P<pk>[0-9]+)/$', views.PropertyDetailView.as_view(), name='detail'),
    
# lookup
    url(r'^lookup/$', views.LookupView.as_view(), name='lookup'),
    
# distance
    url(r'^distance/$', views.DistanceView.as_view(), name='distance'),
    
]