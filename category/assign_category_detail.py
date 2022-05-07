class AssignCategoryDetailsView(LoginRequiredMixin, DetailView):
    template_name = 'category_detail.html'

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        return
