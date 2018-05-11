# transactions/urls.py

from django.conf.urls import url

from . import views

app_name = 'transactions'

urlpatterns = [
    
# E.g., http://localhost:8000/transactions
    url(r'^list/(?P<prop_pk>[0-9]+)/$', views.TransactionListView.as_view(), name='list_by_prop'),

# E.g., http://localhost:8000/transactions/edit/1/
    url(r'^add/$', views.TransactionCreateView.as_view(), name='add'),

# E.g., http://localhost:8000/transactions/edit/1/
    url(r'^edit/(?P<pk>[0-9]+)/$', views.TransactionUpdateView.as_view(), name='edit'),

# E.g., http://localhost:8000/transactions/1/
    url(r'^(?P<pk>[0-9]+)/$', views.TransactionDetailView.as_view(), name='detail'),
]