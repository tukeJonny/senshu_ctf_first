import sys
sys.path.append('../')
import json
import random
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.question'

class Question(object):
    def __init__(self):
        self.category = self.make_category()
        self.title = self.make_title()
        self.description = self.make_description()
        self.solved = self.make_solved()
        self.problem_url = self.make_problem_url()

    def make_category(self):
        #Web, Network, Binary, Forensics, Crypto
        return random.randint(1, 6)

    def make_title(self):
        return gt.generate_randstr(15)

    def make_description(self):
        return gt.generate_randstr(100)

    def make_solved(self):
        return random.randint(0, 20)

    def make_problem_url(self):
        return "http://example.com/{}".format(gt.generate_randstr(30))

    def __str__(self):
        return "<Question: {category}, {title}, {description}, {solved}, {problem_url}>".format(
            category=self.category,
            title=self.title,
            description=self.description,
            solved=self.solved,
            problem_url=self.problem_url
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
