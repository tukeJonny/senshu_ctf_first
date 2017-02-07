#-*- coding: utf-8 -*-

from django import template
from scoreserver.models import Hint
from django.db.models.query import QuerySet

register = template.Library()

@register.filter(name='get_question_hint')
def get_question_hint(question):
    hints = Hint.objects.filter(question=question)
    if len(hints) == 1:
        hints = hints[0]
    elif len(hints) == 0:
        return "No hint."
    return hints

@register.filter(name='iterate_hints')
def iterate_hints(hints):
    for hint in hints:
        yield hint

@register.filter(name='is_queryset')
def is_queryset(obj):
    return isinstance(obj, QuerySet)


