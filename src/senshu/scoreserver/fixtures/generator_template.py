import string
import random

#各モデルで共通のメソッド等を定義する

def generate_randstr(length):
    """
    ランダムな文字列をlengthの長さで返す
    :param length: 文字列の長さ
    :return: ランダムな文字列
    """
    ret = ""
    for c in range(length):
        ret += random.choice(string.ascii_letters)
    return ret


def create_seeddict(model, pk, **fields):
    """
    modelに対し、指定Primary Keyで各モデルのfieldsオブジェクトのレコードを追加するための辞書オブジェクトを返す
    :param model: 対象モデル
    :param pk: レコードのPrimary Key
    :param fields: モデルのフィールド(辞書)
    :return: シードデータの一部となる辞書オブジェクト
    """
    d = {
        "model": model,
        "pk": pk,
        "fields": fields
    }
    return(d)

