from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

from . import views

app_name = 'scoreserver'
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'scoreserver/login.html'}),
    url(r'^logout/$', django.contrib.auth.views.logout, {'template_name': 'scoreserver/logout.html'})
]