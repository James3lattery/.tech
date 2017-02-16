from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views
from auth.forms import LoginForm

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('auth.urls')),
    url(r'^login/$', views.login, {'template_name': 'home.html', 'authentication_form': LoginForm}, name='login'),
]
