from django.core.exceptions import ValidationError

def validate_email(value):
    print("valuedsafds",value)
    if not "@gmail.com" or "@yahoo.com" in value:
        raise ValidationError("A valid email must be entered in")
    else:
        return value