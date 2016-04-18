from django import template

register = template.Library()

@register.filter(name='by')
def by(value, arg):
      return value / arg

@register.filter(name='times')
def by(value, arg):
      return value * arg
