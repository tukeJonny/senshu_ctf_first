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


#Todos
#インデックスページ作成
#問題一覧作成
#問題詳細画面作成(フラグ提出フォームがある)
#ランキング画面作成(Userの獲得ポイントを元に並べてやればおk

#Memos
#@login_requiredデコレータをつけることで、認証が必要なビューを定義できる