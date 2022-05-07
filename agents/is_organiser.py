def get_queryset(self):
    user = self.request.user
    if user.is_organised:
        queryset = models.Lead.objects.filter(organiser=user.userprofile)
    else:
        queryset = models.Lead.objects.filter(organiser=user.agent.organiser)
        queryset = queryset.filter(agent__user=self.request.user)
    return queryset
