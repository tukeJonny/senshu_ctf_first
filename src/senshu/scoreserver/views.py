#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
# Create your views here.

def index(request):
    context = {}
    return render(request, 'scoreserver/index.html', context)

class QuestionIndexView(generic.ListView):
    pass

<<<<<<< HEAD

#Todos
#インデックスページ作成
#問題一覧作成
#問題詳細画面作成(フラグ提出フォームがある)
#ランキング画面作成(Userの獲得ポイントを元に並べてやればおk

#Memos
#@login_requiredデコレータをつけることで、認証が必要なビューを定義できる
=======
def Login(request):
    context={"title":"login"}
    return render(request, 'scoreserver/login.html', context)

def Problems(request):
    context = {}
    return render(request,'scoreserver/problems.html',context)

def ScoreBoard(request):
    context = {"title":"scoreboard"}
    return render(request,'scoreserver/scoreboard.html',context)

def ProblemDetail(request):
    context={}
    return render(request,'scoreserver/problems_detail.html',context)

def Web(request):
	context = {"mondai0":{
                        "title":"mondai0",
                        "main":"main0"
                        },
                "mondai1":{
                        "title":"mondai1",
                        "main":"main1"
                        },
                "title":"web"
    }
	return render(request,'scoreserver/problems.html',context)

def Network(request):
	context={"title":"network"}
	return render(request,'scoreserver/problems.html',context)

def Crypt(request):
	context={"title":"crypt"}
	return render(request,'scoreserver/problems.html',context)

def Forensics(request):
	context={"title":"forensics"}
	return render(request,'scoreserver/problems.html',context)

def Reversing(request):
	context={"title":"reversing"}
	return render(request,'scoreserver/problems.html',context)

def Misc(request):
	context={"title":"misc"}
	return render(request,'scoreserver/problems.html',context)
>>>>>>> 577aa219e030eb49abe1e50a30897a1aa18daf90
