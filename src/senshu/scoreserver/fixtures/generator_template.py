import string
import random

def generate_randstr(length):
    ret = ""
    for c in range(length):
        ret += random.choice(string.ascii_letters)
    return ret


def create_seeddict(model, pk, **fields):
    d = {
        "model": model,
        "pk": pk,
        "fields": fields
    }
    return(d)

