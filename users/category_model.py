from django.db import models

class User(AbstractUser):
    is_organised = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)


# -----xxxxxxxxxxx Category model here  xxxxxxxxxxxxxx------------ #
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Main Category Model'
    category_name = models.CharField(max_length=30)
    organiser = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name
    
# -----xxxxxxxxxxx Category model here  xxxxxxxxxxxxxx------------ #