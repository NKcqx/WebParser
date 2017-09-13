from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^parse/$', views.parseWeb, name = 'parseWeb')
]