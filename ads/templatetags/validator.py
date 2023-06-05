from django import template
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

register = template.Library()

@register.filter(name="validate")
def validate(value):
    url = URLValidator()
    try:
        url(value)
    except ValidationError as e:
        return False
    return True