from django.core.validators import URLValidator
from django.core.exceptions import ValidationError


def validate_url(url):
    urlvalidator = URLValidator()
    try:
        urlvalidator(url)
    except:
        raise ValidationError("Invalid URL.")
    return url

def validate_dot_com(url):
    if "com" not in url:
        raise ValidationError("The url is invalid because of no .com")
    return url