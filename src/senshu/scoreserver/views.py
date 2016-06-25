#-*- coding: utf-8 -*-

from django.utils import timezone
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views import generic
from .models import Question, User, Flag
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
    template_name = 'scoreserver/questions.html' #should modify problems.html -> questions.html
    context_object_name = 'questions'
    def get_queryset(self):
        return Question.objects.all

class ScoreBoardView(generic.TemplateView):
    template_name = "scoreserver/scoreboard.html"

    def get_context_data(self, **kwargs):
        context = super(ScoreBoardView, self).get_context_data(**kwargs)
        context["title"] = "scoreboard"
        context["users"] = User.objects.all().order_by('-points')
        return context

class QuestionDetailView(generic.DetailView):
    template_name = "scoreserver/question_detail.html"
    queryset = Question.objects.all()
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        context['title'] = "Question Detail"
        return context

#基底クラス
class CategoryTemplateView(generic.TemplateView):
    model = Question
    def get_zipped_context_data(self, category):
        """ categoryのquestionsと、それに対応付いたpointsをzipで固めて返す """
        questions = Question.objects.filter(category__name=category) #配列
        points = []
        for question in questions:
            point = -1
            flag = Flag.objects.filter(question=question)
            if len(flag) > 0:
                point = flag[0].point
            points.append(point)
        return(zip(questions, points))


class WebView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        context["title"] = "Web"
        context['zipped_questions_points'] = self.get_zipped_context_data("Web")
        return context

class NetworkView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(NetworkView, self).get_context_data(**kwargs)
        context["title"] = "Network"
        context['zipped_questions_points'] = self.get_zipped_context_data("Network")
        return context

class CryptoView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(CryptoView, self).get_context_data(**kwargs)
        context["title"] = "Crypto"
        context['zipped_questions_points'] = self.get_zipped_context_data("Crypto")
        return context

class ForensicsView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(ForensicsView, self).get_context_data(**kwargs)
        context["title"] = "Forensics"
        context['zipped_questions_points'] = self.get_zipped_context_data("Forensics")
        return context

class BinaryView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(BinaryView, self).get_context_data(**kwargs)
        context["title"] = "Binary"
        context['zipped_questions_points'] = self.get_zipped_context_data("Binary")
        return context

class MiscView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(MiscView, self).get_context_data(**kwargs)
        context["title"] = "Misc"
        context['zipped_questions_points'] = self.get_zipped_context_data("Misc")
        return context

