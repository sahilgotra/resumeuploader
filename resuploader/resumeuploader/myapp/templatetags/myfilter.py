from django import template
register = template.Library()

@register.filter(name='remove_special')
def remove_cars(value, arg):
    print('arg',arg)
    print('value',value)
    for char in arg:
        value = value.replace(char, '')
    return value