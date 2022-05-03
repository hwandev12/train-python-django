class AgentUpdateView(OraniserAndLoginRequiredMixin, generic.UpdateView):
    template_name = 'agents/update.html'
    form_class = AgentCreateModel
    context_object_name = 'agent'

    def get_success_url(self):
        return reverse('agents:agent-lists')

    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)
