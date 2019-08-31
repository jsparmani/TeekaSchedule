from django import template
from parent import models as parent_models

register = template.Library()


@register.filter
def form_loop(value, arg):
    return value[arg]


@register.filter
def child(value):
    x = parent_models.Child.objects.all().filter(
        parent__user__username__exact=value)
    print(value)
    return x
