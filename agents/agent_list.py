class AgentsListView(OraniserAndLoginRequiredMixin, generic.ListView):
    template_name = 'agents/lists.html'
    context_object_name = 'agent'
    
    def get_queryset(self):
        organiser = self.request.user.userprofile
        return Agent.objects.filter(organiser=organiser)