"""elegant_prop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

from core.views import HomeView, SamplePageView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^sample/$', SamplePageView.as_view(), name='sample'),

    # Property related urls.
    url(r'^property/', include('properties.urls')),

    # Transaction related urls.
    url(r'^transaction/', include('transactions.urls')),

    # Messenger related urls.
    url(r'^messenger/', include('messenger.urls')),
    
    url(r'^admin/', admin.site.urls),
]
