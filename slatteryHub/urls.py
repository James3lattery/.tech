from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^files/$', views.upload, name='file'),
    url(r'^notes/$', views.notes, name='notes'),
    url(r'^skyward/$', views.skyward, name='skyward'),
]
