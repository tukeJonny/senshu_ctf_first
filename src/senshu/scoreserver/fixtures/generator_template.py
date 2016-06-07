import random

def generate_randstr(length):
    length = 5
    ret = ""
    for c in range(length):
        ret += chr(random.randint(65, 89))
    return ret


def create_seeddict(model, pk, **fields):
    d = {
        "model": model,
        "pk": pk,
        "fields": fields
    }
    return(d)

