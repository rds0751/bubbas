from django import template
from django.core.files.storage import default_storage
from django.conf import settings

register = template.Library()


@register.filter(name="validate")
def validate(value):
    try:
        print(default_storage.exists(str(settings.BASE_DIR) + value))
    except Exception as e:
        print(e)
        return False
    return True