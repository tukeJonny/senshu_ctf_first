import sys
sys.path.append('../')
import json
import hashlib

import pprint

import generator_template as gt

MODEL_NAME = 'scoreserver.user'

class User(object):
    def __init__(self):
        self.username = self.make_username()
        self.password = self.make_password()

    def make_username(self):
        #Web, Network, Binary, Forensics, Crypto
        return gt.generate_randstr(5)

    def make_password(self):
        return hashlib.sha256(gt.generate_randstr(15).encode("utf-8")).hexdigest()

    def __str__(self):
        return "<User: {username}, {password}>".format(
            username=self.username,
            password=self.password
        )

def get_user_jsondata(NUM):
    print("*"*20 + " User " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        u = User()
        user = gt.create_seeddict(MODEL_NAME, pk, **u.__dict__)
        fixture_list.append(user)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_user_jsondata()
