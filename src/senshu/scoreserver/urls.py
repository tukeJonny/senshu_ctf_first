from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views

from . import views

app_name = 'scoreserver'
urlpatterns = [
<<<<<<< HEAD
    url(r'^admin/', include(admin.site.urls)),
    url(r'^index/$', views.index, name='index'),
    url(r'^login/$', django.contrib.auth.views.login, {'template_name': 'scoreserver/login.html'}),
    url(r'^logout/$', django.contrib.auth.views.logout, {'template_name': 'scoreserver/logout.html'})
]
=======
  url(r'scoreserver/login', views.Login),
  url(r'scoreserver/scoreboard', views.ScoreBoard),
  url(r'scoreserver/problems', views.Problems),
  url(r'scoreserver/problem_detail', views.ProblemDetail),
  url(r'scoreserver/web', views.Web),
  url(r'scoreserver/network', views.Network),
  url(r'scoreserver/crypt', views.Crypt),
  url(r'scoreserver/forensics', views.Forensics),
  url(r'scoreserver/reversing', views.Reversing),
  url(r'scoreserver/misc', views.Misc)
]
>>>>>>> 577aa219e030eb49abe1e50a30897a1aa18daf90
