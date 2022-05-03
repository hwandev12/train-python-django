from django.db import models


class Lead(models.Model):
    class Meta:
        verbose_name = "Lead"
        verbose_name_plural = "Fashion Leads"

    name = models.CharField(max_length=30)
    category = models.ForeignKey(
        'Category', blank=True, related_name='leads', null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Main Category Model'
        
        
    category_name = models.CharField(max_length=30)
    organiser = models.ForeignKey('UserProfile', on_delete=models.CASCADE)

    def __str__(self):
        return self.category_name