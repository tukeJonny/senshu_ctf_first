import sys
sys.path.append('../') # for generator_template

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "senshu.settings")

from scoreserver.models import*

import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.answerhistory'
qnum = 10
unum = 10

class AnswerHistory(object):
    def __init__(self):
        self.user = self.make_user()
        self.question = self.make_question()
        self.submit_flag = self.make_submit_flag()

    def make_question(self):
        return random.randint(1, qnum-1)

    def make_user(self):
        return random.randint(1, unum-1)

    def make_submit_flag(self):
        return "FLAG_IS_{}".format(gt.generate_randstr(15))

    def __str__(self):
        return "<Flag: {user}, {question}, {point}>".format(
            user=self.user,
            question=self.question,
            point=self.point
        )

def get_answerhistory_jsondata(NUM):
    print("*"*20 + " Attack Point History " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        a = AnswerHistory()
        answerhistory = gt.create_seeddict(MODEL_NAME, pk, **a.__dict__)
        fixture_list.append(answerhistory)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_attackpointhistory_jsondata()
