# here you can see that we import login required mixin and accesmixins
from django.contrib.auth.mixins import LoginRequiredMixin, AccessMixin
# here we import redirects to redirect to some urls
from django.shortcuts import redirect

# we called it OrganiserAndLoginRequiredMixin and follow code!
class OraniserAndLoginRequiredMixin(AccessMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated or not request.user.is_organiser:
            return redirect('login')
        return super().dispatch(request, *args, **kwargs)