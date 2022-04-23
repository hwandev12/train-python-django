from django import forms
from .model import YourAgent

# It is for create agent in the main agent folder


class AgentAssignForm(forms.Form):
    agent = forms.ModelChoiceField(queryset=YourAgent.objects.none())

    def __init__(self, *args, **kwargs):
        request = kwargs.pop('request')
        spies = YourAgent.objects.filter(organiser=request.user.userprofile)
        super(AgentAssignForm, self).__init__(*args, **kwargs)
        self.fields['agent'].queryset = spies
