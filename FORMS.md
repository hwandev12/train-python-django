# The simple form of the django

`class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = (
            "name",
            "last_name",
            "email",
            "age",
            "agent",
        )
`
