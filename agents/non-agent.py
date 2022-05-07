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
    # Bu yerda aniqlanmagan agent uchun funksiya yozilgan
