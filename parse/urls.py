from django.conf.urls import include, url
from .views import index, reader

urlpatterns = [
    url(r'^$', index.show, name = 'index'),
    url(r'^parseWeb/$', reader.parseWeb, name = 'parseWeb'),
    url(r'^addWeb/$', index.add, name='addWeb')
]