import sys
sys.path.append('Question/')
sys.path.append('Category/')
sys.path.append('Notice/')
import json

import question_seed_generator as qsg
import category_seed_generator as csg
import notice_seed_generator as nsg

if __name__ == '__main__':
    jsondata = []

    #Category
    jsondata.extend(json.loads(csg.get_category_jsondata()))
    #Question
    jsondata.extend(json.loads(qsg.get_question_jsondata()))
    #Notice
    jsondata.extend(json.loads(nsg.get_notice_jsondata()))

    print(jsondata)
    with open("initial_data.json", "w") as f:
        f.write(json.dumps(jsondata))

