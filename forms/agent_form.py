from dataclasses import fields
from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
# here we are importing form our local models of Agent
from records_feed.models import Agent

User = get_user_model()

class AgentCreateModel(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'email',
            'username',
            'first_name',
            'last_name'
        )