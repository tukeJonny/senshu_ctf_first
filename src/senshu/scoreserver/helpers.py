import json
from scoreserver.models import Question, Flag, AnswerHistory, AttackPointHistory
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ObjectDoesNotExist

import requests
from senshu import settings


def post_to_slack(channel, name, webhook_url, msg, icon_url):
    """
    Slackに、Incoming WebhookでPOSTさせるためのメソッド
    :param channel: Slackのチャンネル
    :param name: 投稿者名
    :param webhook_url: Incoming WebhookのURL
    :param msg: 投稿メッセージ
    :param icon_url: 投稿者の画像アイコンのURL
    :return: Slack Incoming Webhookインテグレーションからのレスポンス
    """
    if webhook_url is not None:
        payload = {
            "channel": channel,
            "username": name,
            "text": msg, #投稿するテキスト
            "icon_url": icon_url, #アイコン画像
        }
        jpayload = json.dumps(payload)
        #あとでrequestsをインスコ
        res = requests.post(webhook_url, jpayload, headers={'Content-Type': 'application/json'})
        return res

class FlagSubmit(object):
    def __init__(self, user, question_id, flag):
        self.user = user
        self.question = Question.objects.get(pk=question_id)
        self.flag_str = flag
        try:
            self.flag = Flag.objects.get(flag=flag)
        except ObjectDoesNotExist:
            self.flag = flag
    def success(self):
        """
        フラグ提出の結果が正解の場合、
        1. 回答履歴を追加
        2. 正解した回答履歴を追加
        3. ユーザの得点を更新
        4. 問題のsolvedをインクリメント
        5. SlackにPOST
        :return: None
        """
        #AnswerHistory
        ah = AnswerHistory(user=self.user, question=self.question, submit_flag=self.flag_str)
        ah.save()
        #AttackPointHistory
        aph = AttackPointHistory(user=self.user, question=self.question, point=self.flag.point)
        aph.save()
        #User
        self.user.update_points()
        self.user.save()
        #Question
        self.question.solved += 1
        self.question.save()
        post_to_slack(settings.SUCCESS_LOG_INCOMING_CHANNEL, settings.SUCCESS_LOG_INCOMING_NAME,settings.SUCCESS_LOG_INCOMING_URL, str(aph), settings.SUCCESS_LOG_INCOMING_IMAGE_URL)

    def fail(self):
        """
        フラグ提出が失敗の場合、
        1. 回答履歴を追加
        2. SlackにPOST
        :return: None
        """
        #AnswerHistory
        ah = AnswerHistory(user=self.user, question=self.question, submit_flag=self.flag_str)
        ah.save()
        post_to_slack(settings.FAIL_LOG_INCOMING_CHANNEL, settings.FAIL_LOG_INCOMING_NAME,settings.FAIL_LOG_INCOMING_URL, str(ah), settings.FAIL_LOG_INCOMING_IMAGE_URL)


def get_ranking_info(request):
    """
    :param request: Viewが受け取るrequestのオブジェクト
    :return: 全ユーザ数及びrequest.userの現在のランクのタプル
    """
    all_user = list(User.objects.filter(is_superuser=False, is_staff=False))
    all_user_num = len(all_user)
    try:
        login_user_rank = all_user.index(request.user)+1 #0,1,2,... -> 1,2,3,...
    except ValueError:
        login_user_rank = -1
    return(all_user_num,login_user_rank)

def is_already_attacked(user, question_id):
    """
    フラグを提出したuserが、過去にquestion_idの問題の正解フラグを提出しているならばTrueを返す
    そうでなければFalseを返す
    :param user: Userオブジェクト
    :param question_id: QuestionのPrimary Key
    :return: userの正解した回答履歴に対応する問題の一覧に、question_idの問題が含まれているか、真偽値で返す
    """
    question = Question.objects.get(pk=question_id)
    #フラグを提出したユーザが今までに攻撃成功した履歴を引っ張ってくる
    try:
        attack_point_history = AttackPointHistory.objects.filter(user=user)
    except Exception:
        attack_point_history = []
    return question in [aph.question for aph in attack_point_history]

def get_user_solved_questions(user):
    """
    :param user: Userオブジェクト
    :return: userが解いた問題の一覧の配列
    """
    #対象ユーザの攻撃成功履歴を取得
    try:
        aphs = AttackPointHistory.objects.filter(user=user)
    except Exception:
        aphs = []
    return [aph.question.id for aph in list(aphs)]

def is_already_exist_user(username):
        """
        同じusernameのユーザの登録を許さない
        :param username: User.username
        :return: 既に登録されているか、その真偽値
        """
        return len(User.objects.filter(username=username)) > 0