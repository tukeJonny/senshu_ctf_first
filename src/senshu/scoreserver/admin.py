#-*- coding: utf-8 -*-
from django.contrib import admin

from .models import Notice, Question, Category, Flag, User, AttackPointHistory, AnswerHistory

# Register your models here.

class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title', 'description']})
    ]
    list_display = ('title', 'description')
    search_fields = ['title']

class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Category Name", {'fields': ['name']})
    ]
    list_display = ('name',)
    search_fields = ['name']

class FlagInline(admin.TabularInline):
    model = Flag
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category', 'title']}),
        ('The number of player who solves this problem', {'fields': ['solved']})
    ]
    inlines = [FlagInline]
    list_display = ('title', 'category', 'solved')
    list_filter = ['solved']
    search_fields = ['title', 'category']

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

admin.site.register(Notice, NoticeAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(AttackPointHistory, AttackPointHistoryAdmin)
admin.site.register(AnswerHistory, AnswerHistoryAdmin)

