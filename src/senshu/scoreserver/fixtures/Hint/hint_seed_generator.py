import sys
sys.path.append('../')
import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.hint'
qnum = 10

class Hint(object):
    def __init__(self):
        self.question = self.make_question()
        self.description = self.make_description()

    def make_question(self):
        return random.randint(1, qnum-1)

    def make_description(self):
        return gt.generate_randstr(100)

    def __str__(self):
        return "<Flag: {question}, {description}>".format(
            question=self.question,
            description=self.description
        )

def get_hint_jsondata(NUM):
    print("*"*20 + " Hint " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        h = Hint()
        hint = gt.create_seeddict(MODEL_NAME, pk, **h.__dict__)
        fixture_list.append(hint)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_hint_jsondata()
