from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views
from . import views
from .views import QuestionListView
from .views import QuestionDetailView
from .views import ScoreBoardView, WebView, NetworkView, CryptoView, ForensicsView, BinaryView, MiscView

app_name = 'scoreserver'
urlpatterns = [
  url(r'scoreserver/login', views.Login),
  url(r'scoreserver/scoreboard', ScoreBoardView.as_view()),
  url(r'scoreserver/questions', QuestionListView.as_view(), name="questions"),
  url(r'scoreserver/question_detail/(?P<pk>\d+)', QuestionDetailView.as_view()),
  url(r'scoreserver/web', WebView.as_view()),
  url(r'scoreserver/network', NetworkView.as_view()),
  url(r'scoreserver/crypt', CryptoView.as_view()),
  url(r'scoreserver/forensics', ForensicsView.as_view()),
  url(r'scoreserver/reversing', BinaryView.as_view()),
  url(r'scoreserver/misc', MiscView.as_view())
]
