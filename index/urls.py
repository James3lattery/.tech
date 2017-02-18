from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('auth.urls')),
    url(r'', include('slatteryHub.urls')),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)