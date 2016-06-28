from django.test import TestCase, Client


# Create your tests here.
class UserViewTests(TestCase):
    """
    ユーザの登録、ログイン、ログアウトが正しくできているかテスト
    """

    def test_login(self):
        pass

    def test_logout(self):
        pass

    def test_register(self):
        pass

class QuestionViewTests(TestCase):
    """
    問題一覧、カテゴリ問題一覧、問題詳細画面等が正しく表示されているかテスト
    """

    def test_questions_list(self):
        pass

    def test_category_questions_list(self):
        pass

    def test_question_detail(self):
        pass

