from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.models import User




class Recipe(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    name = models.CharField(max_length=100)
    description = models.TextField()
    time = models.IntegerField(null=True)
    ingredients1 = models.TextField(max_length=255, null=True, blank=True)
    ingredients2 = models.TextField(max_length=255, null=True, blank=True)
    ingredients3 = models.TextField(max_length=255, null=True, blank=True)
    ingredients4 = models.TextField(max_length=255, null=True, blank=True)
    ingredients5 = models.TextField(max_length=255, null=True, blank=True)

    instructions1 = models.TextField(max_length=255, null=True, blank=True)
    instructions2 = models.TextField(max_length=255, null=True, blank=True)
    instructions3 = models.TextField(max_length=255, null=True, blank=True)
    instructions4 = models.TextField(max_length=255, null=True, blank=True)
    instructions5 = models.TextField(max_length=255, null=True, blank=True)

    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.name



