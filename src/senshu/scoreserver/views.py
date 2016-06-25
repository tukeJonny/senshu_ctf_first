#-*- coding: utf-8 -*-

from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views import generic
from .models import Question, User
# Create your views here.



#Todos
#インデックスページ作成
#問題一覧作成
#問題詳細画面作成(フラグ提出フォームがある)
#ランキング画面作成(Userの獲得ポイントを元に並べてやればおk

#Memos
#@login_requiredデコレータをつけることで、認証が必要なビューを定義できる
def Login(request):
    context={"title":"login"}
    return render(request, 'scoreserver/login.html', context)

class QuestionListView(generic.ListView):
    template_name = 'scoreserver/problems.html' #should modify problems.html -> questions.html
    context_object_name = 'questions'
    def get_queryset(self):
        return Question.objects.all

# def Problems(request):
#     context = {}
#     return render(request,'scoreserver/problems.html',context)

class ScoreBoardView(generic.TemplateView):
    template_name = "scoreserver/scoreboard.html"

    def get_context_data(self, **kwargs):
        context = super(ScoreBoardView, self).get_context_data(**kwargs)
        context["title"] = "scoreboard"
        context["users"] = User.objects.all().order_by('-point')
        #print("Pass: ")
        #print(context)
        return context

# def ScoreBoard(request):
#     context = {"title":"scoreboard"}
#     return render(request,'scoreserver/scoreboard.html',context)

class QuestionDetailView(generic.DetailView):
    template_name = "scoreserver/question.html"
    queryset = Question.objects.all
    context_object_name = "question"


# def ProblemDetail(request):
#     context={}
#     return render(request,'scoreserver/problems_detail.html',context)

class WebView(generic.TemplateView):
    template_name = "scoreserver/web.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        context["title"] = "Web"
        context['web_questions'] = Question.objects.filter(category__name="Web") #配列
        return context

# def Web(request):
# 	context = {"mondai0":{
#                         "title":"mondai0",
#                         "main":"main0"
#                         },
#                 "mondai1":{
#                         "title":"mondai1",
#                         "main":"main1"
#                         },
#                 "title":"web"
#     }
# 	return render(request,'scoreserver/problems.html',context)

class NetworkView(generic.TemplateView):
    template_name = "scoreserver/network.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(NetworkView, self).get_context_data(**kwargs)
        context["title"] = "Network"
        context['network_questions'] = Question.objects.filter(category__name="Network") #配列
        return context

# def Network(request):
# 	context={"title":"network"}
# 	return render(request,'scoreserver/problems.html',context)

class CryptoView(generic.TemplateView):
    template_name = "scoreserver/crypto.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        context["title"] = "Crypto"
        context['crypto_questions'] = Question.objects.filter(category__name="Crypto") #配列
        return context

# def Crypt(request):
# 	context={"title":"crypt"}
# 	return render(request,'scoreserver/problems.html',context)

class ForensicsView(generic.TemplateView):
    template_name = "scoreserver/forensics.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(ForensicsView, self).get_context_data(**kwargs)
        context["title"] = "Forensics"
        context['forensics_questions'] = Question.objects.filter(category__name="Forensics") #配列
        return context

# def Forensics(request):
# 	context={"title":"forensics"}
# 	return render(request,'scoreserver/problems.html',context)

class BinaryView(generic.TemplateView):
    template_name = "scoreserver/binary.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(BinaryView, self).get_context_data(**kwargs)
        context["title"] = "Binary"
        context['binary_questions'] = Question.objects.filter(category__name="Binary") #配列
        return context

# def Reversing(request):
# 	context={"title":"reversing"}
# 	return render(request,'scoreserver/problems.html',context)

class MiscView(generic.TemplateView):
    template_name = "scoreserver/misc.html"
    model = Question
    def get_context_data(self, **kwargs):
        context = super(MiscView, self).get_context_data(**kwargs)
        context["title"] = "Misc"
        context['misc_questions'] = Question.objects.filter(category__name="Misc") #配列
        return context

# def Misc(request):
# 	context={"title":"misc"}
# 	return render(request,'scoreserver/problems.html',context)
