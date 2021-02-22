from django import forms
from .models import User
# from django.core.exceptions import ValidationError
# from .validators import validate_email

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"

# def validate_email(value):
#     if not "@gmail.com" and "@yahoo.com" in value:
#         raise ValidationError("A valid email must be entered in")
#     else:
#         return value