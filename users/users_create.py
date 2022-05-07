class CreateLead(OrganiserAndLoginRequiredMixin, CreateView):
    template_name = 'create.html'
    form_class = LeadForm

    def get_success_url(self):
        return reverse('lead:leads')

    def form_valid(self, form):
        lead = form.save(commit=False)
        lead.organiser = self.request.user.userprofile
        lead.save()
        return super(CreateLead, self).form_valid(form)
