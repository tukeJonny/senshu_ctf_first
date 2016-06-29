#-*- coding: utf-8 -*-

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views import generic
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context import RequestContext
from django.template.loader import get_template
from .models import Question, Flag, AnswerHistory, AttackPointHistory
from django.contrib.auth import get_user_model
User = get_user_model()
from scoreserver.helpers import FlagSubmit, get_ranking_info, is_already_attacked, get_user_solved_questions
from django.db import connection

# Create your views here.

#競技中に行われ無いような操作は<Option>
#Todos
#インデックスページ作成
#問題一覧作成
#問題詳細画面作成(フラグ提出フォームがある)
#ランキング画面作成(Userの獲得ポイントを元に並べてやればおk
#ユーザ登録(CreateUserView)の作成
#<Option>ユーザ登録情報変更(UpdateUserView)の作成
#<Option>ユーザ削除
#フラグが送信されたらそれを受けるCreateAnswerHistoryViewを作って、
#フラグ判定、正解であればAttackPointHistoryを追加、ユーザのPoint計算
#フラグ提出と同じページに飛ばしてCongraturations!って表示
#不正解であれば、フラグ提出ページに飛ばしてWrong...って表示
#問題詳細画面、ちょっと上に寄りすぎ。見辛い
#ログアウトボタン欲しいので、サイドバーに追加するなりして欲しい
#サイドバーだけでなくトップバーを用意し、そこにログアウトボタンとか

#Memos
#@login_requiredデコレータをつけることで、認証が必要なビューを定義できる
def index(request):
    context = {}
    return render(request, 'scoreserver/index.html', context)

def login_view(request):
    template_name = reverse('scoreserver:index')
    if 'next' in request.GET.keys():
        template_name = request.GET['next']
    context=RequestContext(request, {})
    user = None
    print(request.method)
    if request.POST:
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(template_name)
            else:
                context['is_inactive'] = True
        else:
            print("Login failed.")
            context['login_failed'] = True
    context['title'] = "login"
    context['request'] = request
    context['checked_user'] = user
    return render(request, 'scoreserver/login.html', context)

@login_required(login_url="/scoreserver/login")
def logout_view(request):
    template_name = "scoreserver/logout.html"
    logout(request)
    return render(request, template_name, {"logout": True})

@login_required(login_url="/scoreserver/login")
def flag_submit_view(request, question_id):
    context = {}
    context['title'] = "Question Detail"
    flag = request.POST['flag']
    answer = Flag.objects.get(question=question_id).flag
    fs = FlagSubmit(request.user, question_id, flag)
    #まだ正解しておらず、フラグが正しいのであれば攻撃成功とみなす
    if not is_already_attacked(request.user, question_id):
        if flag == answer:
            messages.success(request, "Congraturations! flag is correct!")
            fs.success()
        else:
            messages.warning(request, "Oh... flag is incorrect... please try again!")
            fs.fail()
    else:
        messages.warning(request, "You're already attacked this question.")
    return HttpResponseRedirect(reverse('scoreserver:question_detail', args=(question_id,)))



class RegisterView(generic.edit.CreateView):
    template_name = "scoreserver/register.html"
    model = User
    fields = ['username', 'password']
    success_url = reverse_lazy("scoreserver:index")

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        result = super(RegisterView, self).form_valid(form)
        #super.form_validでは生パスワードを設定してしまうため、こちら側で行う
        registered_user = User.objects.get(username=username)
        registered_user.set_password(password)
        registered_user.save()
        if result:
            messages.success(self.request, "Saved {}!".format(username))
            if self.request.user.is_authenticated(): #ログイン済みであれば
                logout(self.request) #一旦ログアウト
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(self.request, authenticated_user)
            else:
                messages.warning(self.request, "Please login")
            print("Register Executed Queries {}".format(connection.queries))
        else:
            messages.warning(self.request, "Something went wrong... Please contact a system administrator.")
        return result

    def form_invalid(self, form):
        messages.warning(self.request, "Can't saved...")
        return super().form_invalid(form)

#class UserUpdateView(generic.edit.UpdateView):

#---------- sidebar zone -------

class BaseTemplateView(generic.TemplateView):
    """
    問題を表示する画面やスコアボードのビューに対する基底クラス
    """
    def get_context_data(self, **kwargs):
        context = super(BaseTemplateView, self).get_context_data(**kwargs)
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)

class QuestionListView(LoginRequiredMixin, generic.ListView):
    login_url = '/scoreserver/login'
    #redirect_field_name = 'scoreserver/index'
    template_name = 'scoreserver/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        request = context['view'].request
        #context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)
        context['solved_questions'] = get_user_solved_questions(self.request.user)
        questions = Question.objects.all() #配列
        #DoesNotExist例外ハンドラを書くべき
        points = [flag.point for flag in [Flag.objects.get(question=question) for question in questions]]
        context['zipped_questions_points'] = zip(questions, points)
        return context

    def get_queryset(self):
        return Question.objects.all

class ScoreBoardView(LoginRequiredMixin, generic.TemplateView):
    template_name = "scoreserver/scoreboard.html"

    def get_context_data(self, **kwargs):
        context = super(ScoreBoardView, self).get_context_data(**kwargs)
        context["title"] = "scoreboard"
        context["users"] = User.objects.filter(is_superuser=False, is_staff=False)#.order_by('-points')
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)
        return context

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "scoreserver/question_detail.html"
    queryset = Question.objects.all()
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)
        context['title'] = "Question Detail"
        return context

#基底クラス
class CategoryTemplateView(LoginRequiredMixin, generic.TemplateView):
    model = Question
    def get_context_data(self, **kwargs):
        context = super(CategoryTemplateView, self).get_context_data(**kwargs)
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)
        context['solved_questions'] = get_user_solved_questions(self.request.user)
        return context

    def get_zipped_context_data(self, category):
        """ categoryのquestionsと、それに対応付いたpointsをzipで固めて返す """
        questions = Question.objects.filter(category__name=category) #配列
        #DoesNotExist例外ハンドラを書くべき
        #気のせいかもしれないが、questionsと順番があっていないとダメなので、要チェック
        points = [flag.point for flag in [Flag.objects.get(question=question) for question in questions]]
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


