def form_valid(self, form):
    spy = form.cleaned_data['agent']
    lead = Lead.objects.get(id=self.kwargs['pk'])
    lead.spy = spy
    lead.save()
    return super(AgentAssignView, self).form_valid(form)
# Agenti aniqlanmagan user lar uchun class based view
