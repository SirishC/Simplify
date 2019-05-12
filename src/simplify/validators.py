from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def  validate_url(value):
    url_validator = URLValidator()
    try:
        url_validator(value)
    except:
        raise ValidationError("Invalid URL")
    return value
