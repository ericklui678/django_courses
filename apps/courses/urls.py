from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^destroy/(?P<num>\d+)$', views.remove),
    url(r'^confirm/(?P<num>\d+)$', views.confirm),
    url(r'^create$', views.create),
]
