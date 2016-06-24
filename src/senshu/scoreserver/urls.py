from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views
from . import views
from .views import QuestionListView

app_name = 'scoreserver'
urlpatterns = [
  url(r'scoreserver/login', views.Login),
  url(r'scoreserver/scoreboard', views.ScoreBoard),
  url(r'scoreserver/questions', QuestionListView.as_view(), name="questions"),
  url(r'scoreserver/problem_detail', views.ProblemDetail),
  url(r'scoreserver/web', views.Web),
  url(r'scoreserver/network', views.Network),
  url(r'scoreserver/crypt', views.Crypt),
  url(r'scoreserver/forensics', views.Forensics),
  url(r'scoreserver/reversing', views.Reversing),
  url(r'scoreserver/misc', views.Misc)
]
