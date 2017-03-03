from django.conf.urls import url
from . import views
from .views import noteUpdate, noteDelete

urlpatterns = [
    url(r'^files/$', views.upload, name='file'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^skyward/$', views.skyward, name='skyward'),
    url(r'^images/$', views.images, name='images'),
    url('^notes/u/(?P<pk>[\w-]+)$', noteUpdate.as_view(), name='noteUpdate'),
    url('^notes/d/(?P<pk>[\w-]+)$', noteDelete.as_view(), name='noteDelete'),
]
