import sys
sys.path.append('Question/')
sys.path.append('Category/')
import json

import question_seed_generator as qsg
import category_seed_generator as csg

if __name__ == '__main__':
    jsondata = []

    #Category
    jsondata.extend(json.loads(csg.get_category_jsondata()))
    #Questions
    jsondata.extend(json.loads(qsg.get_question_jsondata()))

    print(jsondata)
    with open("initial_data.json", "w") as f:
        f.write(json.dumps(jsondata))

