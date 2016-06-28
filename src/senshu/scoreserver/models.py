#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
# class Notice(models.Model):
#     """ CTF中のお知らせなど """
#     title = models.CharField(max_length=50)
#     description = models.TextField(default='')
#
#     def __str__(self):
#         return "<Notice: {title}, {description}>".format(title=self.title, description=self.description)

class Category(models.Model):
    """ 問題のカテゴリ """
    name = models.CharField(default='', max_length=50, unique=True)

    def __str__(self):
        return self.name

class Question(models.Model):
    """ 問題 """
    category = models.ForeignKey(Category, verbose_name="カテゴリ")
    title = models.CharField(max_length=50)
    description = models.TextField(default='')
    solved = models.IntegerField("解いた人の数", blank=True, null=True)
    url = models.CharField(max_length=50, null=True)

class Flag(models.Model):
    """ 問題の答え(フラグ) """
    question = models.ForeignKey(Question, verbose_name="問題", unique=True)
    flag = models.CharField(max_length=50, unique=True)
    point = models.IntegerField("得点")

class Hint(models.Model):
    """ 問題のヒント """
    question = models.ForeignKey(Question, verbose_name="問題")
    description = models.TextField(default='')

    def __str__(self):
        return self.description

class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        print("create user!")
        if not username:
            raise ValueError("Users must have username!!")

        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, password):
        u = self.create_user(username, password=password)
        u.is_superuser = True
        u.is_staff = True
        u.save(using=self._db)
        return(u)

class User(AbstractBaseUser):
    """ CTFのプレイヤー """
    class Meta:
        ordering = ("-points",)
        db_table = 'scoreserver_user'

    username = models.CharField(default='', max_length=50, unique=False) #システムエラー回避のためunique=Trueを指定
    #password = models.CharField(max_length=128, verbose_name="パスワードハッシュ")
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    USERNAME_FIELD = 'username'
    #PASSWORD_FIELD = 'password'

    objects = UserManager()

    def __unicode__(self):
        return self.username

    def update_points(self):
        """pointsの更新"""
        print("Calculating points....")
        points = 0
        my_attack_point_history = AttackPointHistory.objects.filter(user=self)
        for point in map(lambda mah: mah.point, my_attack_point_history):
            points += point
        self.points = points

    def set_password(self, raw_password):
        """ パスワード設定 """
        self.password = make_password(raw_password)

    def check_password(self, raw_password):
        print("Authenticating...")
        """ 生パスワードのチェック """
        def setter(raw_password):
            """ パスワード更新 """
            self.set_password(raw_password)
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def get_short_name(self):
        return self.username

class AttackPointHistory(models.Model):
    """ 成功した攻撃の履歴 """
    user = models.ForeignKey(User, verbose_name="ユーザ")
    question = models.ForeignKey(Question, verbose_name="問題")
    point = models.IntegerField("得点")

class AnswerHistory(models.Model):
    """ 回答履歴（成功しているかに関わらず） """
    user = models.ForeignKey(User, verbose_name="回答者")
    question = models.ForeignKey(Question, verbose_name="問題")
    submit_flag = models.CharField(max_length=50, verbose_name="提出フラグ")