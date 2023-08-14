import datetime
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter()
def my_media(val):
    if val:
        return f'/media/{val}'
    else:
        return '/media/catalog/dinn_logo_white.png'

