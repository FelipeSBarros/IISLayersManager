from django.conf import settings
from django.template import Library


register = Library()


@register.simple_tag
def get_settings(value, arg=''):
    return getattr(settings, value, arg)
