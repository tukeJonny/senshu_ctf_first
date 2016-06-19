from django.conf.urls import url

from . import views

app_name = 'scoreserver'
urlpatterns = [
  url(r'scoreserver/login', views.login)
]
