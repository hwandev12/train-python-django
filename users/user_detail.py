class DetailsLead(OrganiserAndLoginRequiredMixin, DetailView):
    template_name = 'details.html'
    context_object_name = 'lead'
    queryset = Lead.objects.all()
