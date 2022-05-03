import random
from django.views import generic
from django.core.mail import send_mail
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
# .mixins is actually for agents to show things and hiding
from .mixins import OraniserAndLoginRequiredMixin
from records_feed.models import Agent
from .forms import AgentCreateModel




# here now we can see so many imports that is crucial role to create, assign and more
# each import is used in each files that commited on the agents folder
