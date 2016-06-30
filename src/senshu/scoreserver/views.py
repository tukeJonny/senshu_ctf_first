#-*- coding: utf-8 -*-

from django.core.urlresolvers import reverse, reverse_lazy
from django.shortcuts import render, HttpResponseRedirect, redirect, render_to_response
from django.views import generic
from django.views import generic
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.context import RequestContext
from django.template.loader import get_template
from .models import Question, Flag, AnswerHistory, AttackPointHistory
from .forms import UserUpdateForm
from django.contrib.auth import get_user_model
User = get_user_model()
from scoreserver.helpers import FlagSubmit, get_ranking_info, is_already_attacked, get_user_solved_questions, is_already_exist_user
from django.db import connection

# Create your views here.

#競技中に行われ無いような操作は<Option>
#Todos
#問題詳細画面、ちょっと上に寄りすぎ。見辛い
#ログアウトボタン欲しいので、サイドバーに追加するなりして欲しい
#サイドバーだけでなくトップバーを用意し、そこにログアウトボタンとか
#ログイン時、Remember me 処理

# --- index page ---

def index(request):
    context = {}
    return render(request, 'scoreserver/index.html', context)

# --- login and logout

def login_view(request):
    template_name = reverse('scoreserver:questions')
    #nextが指定されていれば、そこにリダイレクトさせるようにする
    if 'next' in request.GET.keys():
        template_name = request.GET['next']

    context=RequestContext(request, {})
    user = None
    if request.POST: #ログインPOSTしてきているのであれば
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)

        if user is not None: #認証成功かつ
            if user.is_active: #Userが有効
                login(request, user) #ログイン
                return HttpResponseRedirect(template_name) #リダイレクト
            else:
                context['is_inactive'] = True #Userが無効である旨
        else:
            context['login_failed'] = True #ログイン失敗である旨
    context['title'] = "login"
    context['request'] = request
    context['checked_user'] = user #確認済みのユーザ(Template側で認証済みユーザオブジェクトと分けるため)
    return render(request, 'scoreserver/login.html', context)

@login_required(login_url="/scoreserver/login") #ログイン済みでなければ、ログアウトする意味がわからない
def logout_view(request):
    template_name = "scoreserver/logout.html"
    logout(request) #ログアウト
    return render(request, template_name, {"logout": True})

# --- Flag submit ---

@login_required(login_url="/scoreserver/login") #ログインしないとフラグは提出できない
def flag_submit_view(request, question_id):
    context = {}
    context['title'] = "Question Detail"
    flag = request.POST['flag'] #提出されてきたフラグを取得
    answer = Flag.objects.get(question=question_id).flag #正解のフラグをDBから取得
    fs = FlagSubmit(request.user, question_id, flag) #フラグ提出管理インスタンス生成
    #まだ正解しておらず、フラグが正しいのであれば攻撃成功とみなす
    if not is_already_attacked(request.user, question_id):
        if flag == answer: #正解した
            messages.success(request, "Congraturations! flag is correct!") #正解した旨
            fs.success() #正解時の処理を行う
        else:
            messages.warning(request, "Oh... flag is incorrect... please try again!") #不正解だった旨
            fs.fail() #不正解時の処理を行う
    else:
        messages.warning(request, "You're already attacked this question.") #既にこの問題に対し、攻撃が成功済みである
    return HttpResponseRedirect(reverse('scoreserver:question_detail', args=(question_id,))) #同じ画面に飛ばして、メッセージを表示させる

# --- User Views (Register, Update, Delete) ---

class RegisterView(generic.edit.CreateView):
    template_name = "scoreserver/register.html"
    model = User
    fields = ['username', 'password']
    success_url = reverse_lazy("scoreserver:index")

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        if is_already_exist_user(username):
            messages.warning(self.request, "This user had already registered!!")
            return redirect(reverse_lazy("scoreserver:register"))
        result = super(RegisterView, self).form_valid(form)
        #super.form_validでは生パスワードを設定してしまうため、こちら側で行う
        registered_user = User.objects.get(username=username)
        registered_user.set_password(password)
        registered_user.save()
        if result: #フォームのバリデーションに引っかからなかったら、一緒にログイン処理もこちら側で行ってしまう
            messages.success(self.request, "Saved {}!".format(username))
            if self.request.user.is_authenticated(): #ログイン済みであれば
                logout(self.request) #一旦ログアウト
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(self.request, authenticated_user)
            else:
                messages.warning(self.request, "Please login")
            print("Register Executed Queries {}".format(connection.queries))
        else: #引っかかった
            messages.warning(self.request, "Something went wrong... Please contact a system administrator.")
        return result

    def form_invalid(self, form):
        messages.warning(self.request, "Can't saved...")
        return super().form_invalid(form)

class UserUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """
    ユーザ更新(Profile)用のビュー
    ユーザは、ユーザ名とパスワードの変更が可能である
    """
    slug_field = 'user_id'
    slug_url_kwarg = 'user_id'
    model = User
    form_class = UserUpdateForm
    template_name = "scoreserver/profile.html"
    success_url = reverse_lazy('scoreserver:index')

    def form_valid(self, form):
        username = self.request.POST["username"]
        password = self.request.POST["password"]
        if is_already_exist_user(username):
            messages.warning(self.request, "This user had already registered!!")
            return redirect(reverse_lazy("scoreserver:profile"))
        result = super(UserUpdateView, self).form_valid(form)
        #super.form_validでは生パスワードを設定してしまうため、こちら側で行う
        updated_user = User.objects.get(username=username)
        updated_user.set_password(password)
        updated_user.save()
        if result: #フォームのバリデーションに引っかからなかったら、一緒にログイン処理もこちら側で行ってしまう
            messages.success(self.request, "Saved {}!".format(username))
            if self.request.user.is_authenticated(): #ログイン済みであれば
                logout(self.request) #一旦ログアウト
            authenticated_user = authenticate(username=username, password=password)
            if authenticated_user is not None:
                login(self.request, authenticated_user)
            else:
                messages.warning(self.request, "Please login")
            print("Register Executed Queries {}".format(connection.queries))
        else: #引っかかった
            messages.warning(self.request, "Something went wrong... Please contact a system administrator.")
        return result

    def get_queryset(self):
        queryset = super(UserUpdateView, self).get_queryset()
        return queryset.filter(pk=self.request.user.pk)

    def get_context_data(self, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(self.request.GET, instance=self.request.user)
        return context

    def get(self, request, *args, **kwargs):
        super(UserUpdateView, self).get(request, *args, **kwargs)
        form = self.form_class
        context = self.get_context_data(object=self.object, form=form)
        return self.render_to_response(context)

# --- Question Views ---

class QuestionListView(LoginRequiredMixin, generic.ListView):
    """
    Question一覧を表示するビュー
    """
    login_url = '/scoreserver/login'
    #redirect_field_name = 'scoreserver/index'
    template_name = 'scoreserver/questions.html'
    context_object_name = 'questions'

    def get_context_data(self, **kwargs):
        context = super(QuestionListView, self).get_context_data(**kwargs)
        #for sidebar
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)

        #for question, questions
        context['solved_questions'] = get_user_solved_questions(self.request.user)
        questions = Question.objects.all() #配列
        #DoesNotExist例外ハンドラを書くべき
        points = [flag.point for flag in [Flag.objects.get(question=question) for question in questions]]
        context['zipped_questions_points'] = zip(questions, points)
        return context

    def get_queryset(self):
        return Question.objects.all

class ScoreBoardView(LoginRequiredMixin, generic.TemplateView):
    """
    スコアボードを表示するビュー
    """
    template_name = "scoreserver/scoreboard.html"

    def get_context_data(self, **kwargs):
        context = super(ScoreBoardView, self).get_context_data(**kwargs)
        #for sidebar
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)

        #for scoreboard
        context["title"] = "scoreboard"
        context["users"] = User.objects.filter(is_superuser=False, is_staff=False)#.order_by('-points')
        return context

class QuestionDetailView(LoginRequiredMixin, generic.DetailView):
    """
    Questionの詳細画面を表示するビュー
    """
    template_name = "scoreserver/question_detail.html"
    queryset = Question.objects.all()
    context_object_name = "question"

    def get_context_data(self, **kwargs):
        context = super(QuestionDetailView, self).get_context_data(**kwargs)
        #for sidebar
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)

        #for question_detail
        context['title'] = "Question Detail"
        return context

#基底クラス
class CategoryTemplateView(LoginRequiredMixin, generic.TemplateView):
    """
    カテゴリ(Web, Network, Crypto, Forensics, Binary, Misc)の基底クラス
    """
    model = Question
    def get_context_data(self, **kwargs):
        context = super(CategoryTemplateView, self).get_context_data(**kwargs)
        #for sidebar
        request = context['view'].request
        context['all_user_num'], context['login_user_rank'] = get_ranking_info(request)
        context['solved_questions'] = get_user_solved_questions(self.request.user)
        return context

    def get_zipped_context_data(self, category):
        """
        categoryのquestionsと、それに対応付いたpointsをzipで固めて返す
        :param category: カテゴリの文字列("Web", "Network", ...)
        :return: #categoryの問題(questions)とその問題の得点(points)をzipで固めて返す
        """
        questions = Question.objects.filter(category__name=category) #配列
        #DoesNotExist例外ハンドラを書くべき
        #気のせいかもしれないが、questionsと順番があっていないとダメなので、要チェック
        points = [flag.point for flag in [Flag.objects.get(question=question) for question in questions]]
        return(zip(questions, points))


class WebView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(WebView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Web"
        context['zipped_questions_points'] = self.get_zipped_context_data("Web")
        return context

class NetworkView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(NetworkView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Network"
        context['zipped_questions_points'] = self.get_zipped_context_data("Network")
        return context

class CryptoView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(CryptoView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Crypto"
        context['zipped_questions_points'] = self.get_zipped_context_data("Crypto")
        return context

class ForensicsView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(ForensicsView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Forensics"
        context['zipped_questions_points'] = self.get_zipped_context_data("Forensics")
        return context

class BinaryView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(BinaryView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Binary"
        context['zipped_questions_points'] = self.get_zipped_context_data("Binary")
        return context

class MiscView(CategoryTemplateView):
    template_name = "scoreserver/question.html"
    def get_context_data(self, **kwargs):
        context = super(MiscView, self).get_context_data(**kwargs)
        #for question
        context["title"] = "Misc"
        context['zipped_questions_points'] = self.get_zipped_context_data("Misc")
        return context

#--- error handler ---
def not_found(request):
    response = render_to_response('404.html', context_instance=RequestContext(request))
    response.status_code = 404
    return response

def forbidden(request):
    response = render_to_response('403.html', context_instance=RequestContext(request))
    response.status_code = 403
    return response