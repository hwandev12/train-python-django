class AgentAssignView(OrganiserAndLoginRequiredMixin, FormView):
    template_name = 'assign_agent.html'
    form_class = AgentAssignForm

    def get_form_kwargs(self, **kwargs):
        kwargs = super(AgentAssignView, self).get_form_kwargs(**kwargs)
        kwargs.update({
            'request': self.request
        })
        return kwargs

    def get_success_url(self):
        return reverse('lead:leads')

    def form_valid(self, form):
        spy = form.cleaned_data['agent']
        lead = Lead.objects.get(id=self.kwargs['pk'])
        lead.spy = spy
        lead.save()
        return super(AgentAssignView, self).form_valid(form)
    # Agenti aniqlanmagan user lar uchun class based view
