import sys
sys.path.append('../')
import json
import generator_template as gt
import pprint

MODEL_NAME = "scoreserver.notice"

class Notice(object):
    def __init__(self):
        self.title = self.make_title()
        self.description = self.make_description()

    def make_title(self):
        return gt.generate_randstr(15)

    def make_description(self):
        return gt.generate_randstr(100)

    def __str__(self):
        return "<Notice: {title}, {description}".format(
            title=self.title,
            description=self.description
        )

def get_notice_jsondata(NUM):
    print("*"*20 + " Notice " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        n = Notice()
        notice = gt.create_seeddict(MODEL_NAME, pk, **n.__dict__)
        fixture_list.append(notice)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    #pass
    get_notice_jsondata()