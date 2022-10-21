from django import template
from django.template import Library
register = template.Library()

@register.filter(name ='remove_special')

def remove_character(value,arg):
    for character in arg:
        value = value.replace(character,'')
    return value