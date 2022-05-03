class AgentDetailView(OraniserAndLoginRequiredMixin, generic.DetailView):
    template_name = 'agents/details.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)