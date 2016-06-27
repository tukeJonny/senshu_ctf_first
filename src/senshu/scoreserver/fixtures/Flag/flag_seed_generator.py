import sys
sys.path.append('../')
import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.flag'
qnum = 10

class Flag(object):
    def __init__(self):
        self.question = self.make_question()
        self.point = self.make_point()
        self.flag = self.make_flag()

    def make_question(self):
        #Web, Network, Binary, Forensics, Crypto
        return random.randint(1, qnum-1)

    def make_flag(self):
        #return "FLAG_IS_[{}]".format(gt.generate_randstr(15))
        return "FLAG_IS_[{}]".format(self.point)

    def make_point(self):
        return random.randint(1, 11) * 100

    def __str__(self):
        return "<Flag: {question}, {flag}, {point}>".format(
            question=self.question,
            flag=self.flag,
            point=self.point
        )

def get_flag_jsondata(NUM):
    print("*"*20 + " Flag " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        f = Flag()
        flag = gt.create_seeddict(MODEL_NAME, pk, **f.__dict__)
        fixture_list.append(flag)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_flag_jsondata()
