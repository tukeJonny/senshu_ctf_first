from django.conf.urls import url, include
from django.contrib import admin
import django.contrib.auth.views as auth_views
from . import views
from .views import QuestionListView
from .views import QuestionDetailView
from .views import ScoreBoardView, WebView, NetworkView, CryptoView, ForensicsView, BinaryView, MiscView

#auth_view.login, {'template_name': "scoreserver/login.html"}

app_name = 'scoreserver'
urlpatterns = [
    url(r'^scoreserver/index/$', views.index, name="index"),
    url(r'^scoreserver/login/$', views.login_view, name="login"),
    url(r'^scoreserver/logout/$', views.logout_view,  name="logout"),
    url(r'^scoreserver/scoreboard/$', ScoreBoardView.as_view(), name="scoreboard"),
    url(r'^scoreserver/questions/$', QuestionListView.as_view(), name="questions"),
    url(r'^scoreserver/question_detail/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name="question_detail"),
    url(r'^scoreserver/web/$', WebView.as_view(), name="web"),
    url(r'^scoreserver/network/$', NetworkView.as_view(), name="network"),
    url(r'^scoreserver/crypt/$', CryptoView.as_view(), name="crypt"),
    url(r'^scoreserver/forensics/$', ForensicsView.as_view(), name="forensics"),
    url(r'^scoreserver/reversing/$', BinaryView.as_view(), name="reversing"),
    url(r'^scoreserver/misc/$', MiscView.as_view(), name="misc")
]
