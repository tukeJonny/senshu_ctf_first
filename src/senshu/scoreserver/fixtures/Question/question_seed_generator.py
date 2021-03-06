import sys
sys.path.append('../')
import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.question'
cnum = 6

class Question(object):
    def __init__(self):
        self.category = self.make_category()
        self.title = self.make_title()
        self.description = self.make_description()
        self.solved = self.make_solved()
        self.url = self.make_url()

    def make_category(self):
        return random.randint(1, cnum)

    def make_title(self):
        return "Question_title:"+gt.generate_randstr(15)

    def make_description(self):
        return "Question_desc:"+gt.generate_randstr(100)

    def make_solved(self):
        return 0#random.randint(0, 20)

    def make_url(self):
        return "http://example.com/{}".format(gt.generate_randstr(30))

    def make_hint(self):
        pass

    def __str__(self):
        return "<Question: {category}, {title}, {description}, {solved}, {url}>".format(
            category=self.category,
            title=self.title,
            description=self.description,
            solved=self.solved,
            url=self.url
        )

def get_question_jsondata(NUM):
    print("*"*20 + " Question " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        q = Question()
        question = gt.create_seeddict(MODEL_NAME, pk, **q.__dict__)
        fixture_list.append(question)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_question_jsondata()
