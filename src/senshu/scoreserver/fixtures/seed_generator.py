import sys
sys.path.append('Question/')
sys.path.append('Category/')
sys.path.append('Notice/')
sys.path.append('Flag/')
sys.path.append('User/')
sys.path.append('Hint/')
sys.path.append('AttackPointHistory/')
sys.path.append('AnswerHistory/')
import json

import question_seed_generator as qsg
import category_seed_generator as csg
import notice_seed_generator as nsg
import flag_seed_generator as fsg
import user_seed_generator as usg
import hint_seed_generator as hsg
import attack_point_history_seed_generator as aphsg
import answer_history_seed_generator as ahsg

from django.core.management.base import BaseCommand, CommandError

question_num = 10
notice_num = 10
flag_num = 50
user_num = 10
hint_num = 10
attack_point_history_num = 10
answer_history_num = 10

def main():
    jsondata = []

    qsg.cnum = 6 #fixed
    fsg.qnum = question_num
    hsg.qnum = question_num
    aphsg.unum = user_num
    ahsg.unum = user_num

    #Category
    jsondata.extend(json.loads(csg.get_category_jsondata()))
    #Question
    jsondata.extend(json.loads(qsg.get_question_jsondata(question_num)))
    #Notice
    jsondata.extend(json.loads(nsg.get_notice_jsondata(notice_num)))
    #Flag
    jsondata.extend(json.loads(fsg.get_flag_jsondata(flag_num)))
    #User
    jsondata.extend(json.loads(usg.get_user_jsondata(user_num)))
    #Hint
    jsondata.extend(json.loads(hsg.get_hint_jsondata(hint_num)))
    #Attack Point History
    jsondata.extend(json.loads(aphsg.get_attackpointhistory_jsondata(attack_point_history_num)))
    #Answer History
    jsondata.extend(json.loads(ahsg.get_answerhistory_jsondata(answer_history_num)))


    print(jsondata)
    with open("scoreserver/fixtures/initial_data.json", "w") as f:
        f.write(json.dumps(jsondata))

if __name__ == "__main__":
    main()