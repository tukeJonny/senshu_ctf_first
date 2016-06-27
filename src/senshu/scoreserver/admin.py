#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Question, Category, Flag, Hint, AttackPointHistory, AnswerHistory #, Notice
from django.contrib.auth import get_user_model
User = get_user_model()
# Register your models here.

# class NoticeAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['title', 'description']})
#     ]
#     list_display = ('title', 'description')
#     search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Name", {'fields': ['name']})
    ]
    list_display = ('name',)
    search_fields = ['name']

class FlagInline(admin.TabularInline):
    model = Flag
    extra = 3

class HintInline(admin.TabularInline):
    model = Hint
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category', 'title']}),
        ('問題URL', {'fields': ['problem_url']}),
        ('正解者数', {'fields': ['solved']})
    ]
    inlines = [FlagInline, HintInline]
    list_display = ('title', 'category', 'solved', 'problem_url')
    list_filter = ['solved']
    search_fields = ['title', 'category__name', 'problem_url']

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['username']}),
        ("Hashed Password For Login", {'fields': ['password']})
    ]
    list_display = ('username', 'password', 'is_active')
    list_filter = ['is_active']
    search_fields = ['username']


class AttackPointHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'question', 'point']})
    ]
    list_display = ('user', 'question', 'point')
    search_fields = ['user', 'question']

class AnswerHistoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['user', 'question']}),
        ("提出フラグ", {'fields': ['submit_flag']})
    ]
    list_display = ('user', 'question', 'submit_flag')
    search_fields = ['user', 'question', 'submit_flag']

#admin.site.register(Notice, NoticeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(AttackPointHistory, AttackPointHistoryAdmin)
admin.site.register(AnswerHistory, AnswerHistoryAdmin)

