from django import template
from news.models import New

register = template.Library()

@register.simple_tag
def get_new_list():
    news = New.objects.all()
    return news