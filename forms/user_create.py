from .models import YourModel
from django import forms


class LeadForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = (
            "name",
            "last_name",
            "email",
            "age",
            "agent",
        )
