class AgentCreateView(OraniserAndLoginRequiredMixin, generic.CreateView):
    template_name = 'agents/create.html'
    form_class = AgentCreateModel
    
    def get_success_url(self):
        return reverse('agents:agent-lists')
    
    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_organiser = False
        user.is_agent = True
        user.set_password(f"{random.randint(0, 10000)}")
        user.save()
        Agent.objects.create(
            user=user,
            organiser=self.request.user.userprofile
        )
        send_mail(
            subject='This user has been created',
            message='Created New User',
            from_email='husan3445@gmail.com',
            recipient_list=[user.email]
        )
        # agent.organiser = self.request.user.userprofile
        return super(AgentCreateView, self).form_valid(form)