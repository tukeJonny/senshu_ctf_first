from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

class QuestionIndexView(generic.ListView):
    pass

def login(request):
    context = {}
    return render(request, 'scoreserver/login.html', context)
'''
def Problems:
  None

def ScoreBoard:
  None

def ProblemDetail:
  None
'''
