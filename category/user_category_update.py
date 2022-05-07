class LeadCategoryUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'category_update.html'
    form_class = LeadCategoryUpdateForm

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Lead.objects.filter(
                organiser=user.spy.organiser)
        return queryset

    def get_success_url(self):
        return reverse('lead:leads')
