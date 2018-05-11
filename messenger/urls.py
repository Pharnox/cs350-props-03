# messenger/urls.py

from django.conf.urls import url

from . import views

app_name = 'messenger'

urlpatterns = [
# E.g., http://localhost/messenger/list
    url(r'^list/$', views.MessageListView.as_view(), name='list'),
]