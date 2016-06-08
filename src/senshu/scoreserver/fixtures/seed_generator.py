import sys
sys.path.append('Question/')
sys.path.append('Category/')
sys.path.append('Notice/')
sys.path.append('Flag/')
sys.path.append('User/')
import json

import question_seed_generator as qsg
import category_seed_generator as csg
import notice_seed_generator as nsg
import flag_seed_generator as fsg
import user_seed_generator as usg

if __name__ == '__main__':
    jsondata = []

    #Category
    jsondata.extend(json.loads(csg.get_category_jsondata()))
    #Question
    jsondata.extend(json.loads(qsg.get_question_jsondata(10)))
    #Notice
    jsondata.extend(json.loads(nsg.get_notice_jsondata(10)))
    #Flag
    jsondata.extend(json.loads(fsg.get_flag_jsondata(10)))
    #User
    jsondata.extend(json.loads(usg.get_user_jsondata(10)))

    print(jsondata)
    with open("initial_data.json", "w") as f:
        f.write(json.dumps(jsondata))

