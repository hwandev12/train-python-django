class CategoryAssignView(LoginRequiredMixin, ListView):
    template_name = 'category.html'
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):  # Eslab qolish
        context = super(CategoryAssignView, self).get_context_data(**kwargs)
        user = self.request.user
        if user.is_organised:
            queryset = Lead.objects.filter(
                organiser=user.userprofile
            )
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        context.update({
            'unassigned_category_quantity': queryset.filter(category__isnull=True).count()
        })
        return context

    def get_queryset(self):
        user = self.request.user
        if user.is_organised:
            queryset = Category.objects.filter(
                organiser=user.userprofile)
        else:
            queryset = Category.objects.filter(
                organiser=user.spy.organiser)
        return queryset
