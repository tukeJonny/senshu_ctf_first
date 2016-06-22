from django.conf.urls import url

from . import views

app_name = 'scoreserver'
urlpatterns = [
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
