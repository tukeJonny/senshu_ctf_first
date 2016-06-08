import sys
sys.path.append('../')
import json
import generator_template as gt
import pprint

MODEL_NAME = 'scoreserver.category'
categories = ['Web', 'Network', 'Binary', 'Forensics', 'Crypto', 'Misc']

def get_category_jsondata():
    print("*"*20 + " Category " + "*"*20)
    fixture_list = []
    for pk, category in enumerate(categories):
        fields = {
            "name": category
        }
        question = gt.create_seeddict(MODEL_NAME, pk+1, **fields)
        fixture_list.append(question)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)


if __name__ == "__main__":
    #pass
    get_category_jsondata()