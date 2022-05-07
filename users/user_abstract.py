from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    is_organised = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
