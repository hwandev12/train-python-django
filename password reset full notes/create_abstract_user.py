from django.contrib.auth.models import AbstractUser
from django.db import models


# This is how to create abstract user ans is_organiser is_agent model
class User(AbstractUser):
    is_organised = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
