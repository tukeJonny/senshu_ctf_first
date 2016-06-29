import json
from scoreserver.models import Question, Flag, AnswerHistory, AttackPointHistory
from django.contrib.auth import get_user_model
User = get_user_model()
from django.core.exceptions import ObjectDoesNotExist

import requests

test_incoming_url = None

def post_to_slack(channel, name, webhook_url, msg, icon_url):
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
        post_to_slack("#jvn_alert", "success_log",test_incoming_url, str(aph), "http://p.twpl.jp/show/orig/aqrNm")

    def fail(self):
        #AnswerHistory
        ah = AnswerHistory(user=self.user, question=self.question, submit_flag=self.flag_str)
        ah.save()
        post_to_slack("#jvn_alert", "fail_log",test_incoming_url, str(ah), "http://p.twpl.jp/show/orig/aqrNm")


def get_ranking_info(request):
    all_user = list(User.objects.filter(is_superuser=False, is_staff=False))
    #import pdb; pdb.set_trace()
    all_user_num = len(all_user)
    login_user_rank = all_user.index(request.user)+1 #0,1,2,... -> 1,2,3,...
    return(all_user_num,login_user_rank)

def is_already_attacked(user, question_id):
    """
    フラグを提出したuserが、過去にquestion_idの問題の正解フラグを提出しているならばTrueを返す
    そうでなければFalseを返す
    :param user:
    :param question_id:
    :return:
    """
    question = Question.objects.get(pk=question_id)
    #フラグを提出したユーザが今までに攻撃成功した履歴を引っ張ってくる
    attack_point_history = AttackPointHistory.objects.filter(user=user)
    return question in [aph.question for aph in attack_point_history]

def get_user_solved_questions(user):
    #対象ユーザの攻撃成功履歴を取得
    aphs = AttackPointHistory.objects.filter(user=user)
    return [aph.question.id for aph in list(aphs)]