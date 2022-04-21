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
# Register Form
`
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username",)
        field_classes = {'username': UsernameField}
`
