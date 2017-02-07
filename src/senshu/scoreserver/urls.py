from django.conf.urls import url, include, handler403, handler404
from django.contrib import admin
import django.contrib.auth.views as auth_views
from . import views
from .views import QuestionListView
from .views import QuestionDetailView
from .views import ScoreBoardView, WebView, NetworkView, CryptoView, ForensicsView, BinaryView, MiscView
from .views import RegisterView

handler404 = 'scoreserver.views.not_found'
handler403 = 'scoreserver.views.forbidden'

app_name = 'scoreserver'
urlpatterns = [
    #index page
    url(r'^index/$', views.index, name="index"),
    #login and logout
    url(r'^login', views.login_view, name="login"),
    url(r'^logout/$', views.logout_view,  name="logout"),
    #scoreboard
    url(r'^scoreboard/$', ScoreBoardView.as_view(), name="scoreboard"),
    #User create, update, delete
    url(r'^register/$', RegisterView.as_view(), name="register"),
    #flag submit
    url(r'^submit/(?P<question_id>\d+)/$', views.flag_submit_view, name="submit"),
    #question list, detail, each category
    url(r'^questions/$', QuestionListView.as_view(), name="questions"),
    url(r'^question_detail/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name="question_detail"),
    url(r'^web/$', WebView.as_view(), name="web"),
    url(r'^network/$', NetworkView.as_view(), name="network"),
    url(r'^crypt/$', CryptoView.as_view(), name="crypt"),
    url(r'^forensics/$', ForensicsView.as_view(), name="forensics"),
    url(r'^reversing/$', BinaryView.as_view(), name="reversing"),
    url(r'^misc/$', MiscView.as_view(), name="misc")
]
