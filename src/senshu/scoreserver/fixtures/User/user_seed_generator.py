import sys
sys.path.append('../')
import json
from django.contrib.auth import hashers as hashers

import pprint

import generator_template as gt

MODEL_NAME = 'scoreserver.user'

class User(object):
    def __init__(self, pk):
        self.username = self.make_username(pk)
        self.password = self.make_password(pk)

    def make_username(self, pk):
        #Web, Network, Binary, Forensics, Crypto
        return "user{}".format(pk)

    def make_password(self, pk):
        return hashers.make_password("password{}".format(pk))

    def __str__(self):
        return "<User: {username}, {password}>".format(
            username=self.username,
            password=self.password
        )

def get_user_jsondata(NUM):
    print("*"*20 + " User " + "*"*20)
    fixture_list = []
    for pk in range(NUM):
        u = User(pk)
        user = gt.create_seeddict(MODEL_NAME, pk, **u.__dict__)
        fixture_list.append(user)
    jsondata = json.dumps(fixture_list)
    pprint.pprint(jsondata)
    print("*"*20 + " Finish! " + "*"*20 + "\n")
    return(jsondata)

if __name__ == "__main__":
    pass
    #get_user_jsondata()
