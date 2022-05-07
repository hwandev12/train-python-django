class Leads(LoginRequiredMixin, ListView):
    template_name = 'leads_info.html'
    context_object_name = 'leads'

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = models.Lead.objects.filter(organiser=user.userprofile)
        else:
            queryset = models.Lead.objects.filter(organiser=user.spy.organiser)
            queryset = queryset.filter(spy__user=self.request.user)
        return queryset

    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan
    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(Leads, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile,
                spy__isnull=True
            )
            context.update({
                'unassigned_leads': queryset
            })
            return context
