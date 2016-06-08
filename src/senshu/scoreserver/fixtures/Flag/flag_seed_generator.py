import sys
sys.path.append('../')
import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.flag'

class Question(object):
    def __init__(self):
        self.question = self.make_question()
        self.flag = self.make_flag()
        self.point = self.make_point()

    def make_question(self):
        #Web, Network, Binary, Forensics, Crypto
        return random.randint(1, 10)

    def make_flag(self):
        return "FLAG_IS_[{}]".format(gt.generate_randstr(15))

    def make_point(self):
        return random.randint(100, 1000)

    def __str__(self):
        return "<Question: {category}, {title}, {description}, {solved}, {problem_url}>".format(
            question=self.question,
            flag=self.flag,
            point=self.point
        )

def get_flag_jsondata(NUM):
    print("*"*20 + " Flag " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        f = Question()
        flag = gt.create_seeddict(MODEL_NAME, pk, **f.__dict__)
        fixture_list.append(flag)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20)
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_flag_jsondata()
