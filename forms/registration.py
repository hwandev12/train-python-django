from django.contrib.auth.forms import UserCreationForm, UsernameField
from .models import YourUser


class RegisterForm(UserCreationForm):
    class Meta:
        model = YourUser
        fields = ("username",)
        field_classes = {'username': UsernameField}
