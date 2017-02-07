#-*- coding: utf-8 -*-

from django import template
from scoreserver.models import Hint

register = template.Library()
print("custom filter loaded")

@register.filter(name='get_question_hint')
def get_question_hint(question):
    print("custom filter loaded")
    try:
        hint = Hint.objects.get(question=question)
        return hint.description
    except Hint.DoesNotExist:
        return "No hint."



