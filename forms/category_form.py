from django import forms
from .models import YourModel


class LeadCategoryUpdateForm(forms.ModelForm):
    class Meta:
        model = YourModel
        fields = (
            'category',
        )
