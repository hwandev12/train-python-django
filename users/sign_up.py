from .forms import RegisterForm

class SignupView(CreateView):
    template_name = 'registration/signup.html'
    form_class = RegisterForm

    def get_success_url(self):
        return reverse('lead:leads')