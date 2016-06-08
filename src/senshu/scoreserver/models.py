#-*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='')

class Category(models.Model):
    name = models.CharField(default='', max_length=50, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, verbose_name="カテゴリ")
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    #blank=Trueはどういう意味?
    solved = models.IntegerField("解いた人の数", blank=True, null=True)
    problem_url = models.CharField(max_length=50, null=True)

class Flag(models.Model):
    question = models.ForeignKey(Question, verbose_name="問題")
    flag = models.CharField(max_length=50)
    point = models.IntegerField("得点")

class User(models.Model):
    username = models.CharField(default='', max_length=50)
    login_username = models.CharField(max_length=50)
    login_password_hash = models.CharField(max_length=128, verbose_name="パスワードハッシュ")

    @property
    def hash_password(self):
        pass

class AttackPointHistory(models.Model):
    user = models.ForeignKey(User, verbose_name="ユーザ")
    question = models.ForeignKey(Question, verbose_name="問題")
    point = models.IntegerField("得点")

class AnswerHistory(models.Model):
    user = models.ForeignKey(User, verbose_name="回答者")
    question = models.ForeignKey(Question, verbose_name="問題")
    submit_flag = models.CharField(max_length=50, verbose_name="提出フラグ")