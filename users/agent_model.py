
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save


class User(AbstractUser):
    is_organised = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
    
    
# -----xxxxxxxxxxx Agent model here  xxxxxxxxxxxxxx------------ # 
class Spy(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
# -----xxxxxxxxxxx Agent model here  xxxxxxxxxxxxxx------------ #
