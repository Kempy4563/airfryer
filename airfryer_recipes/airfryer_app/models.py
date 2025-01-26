from django.db import models
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib.auth.models import User
from django.utils import timezone



class Recipe(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, default=1)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    time = models.IntegerField(null=True)
    ingredients1 = models.CharField(max_length=200, null=True, blank=True)
    ingredients2 = models.CharField(max_length=200, null=True, blank=True)
    ingredients3 = models.CharField(max_length=200, null=True, blank=True)
    ingredients4 = models.CharField(max_length=200, null=True, blank=True)
    ingredients5 = models.CharField(max_length=200, null=True, blank=True)
    ingredients6 = models.CharField(max_length=200, null=True, blank=True)
    ingredients7 = models.CharField(max_length=200, null=True, blank=True)

    instructions1 = models.CharField(max_length=400, null=True, blank=True)
    instructions2 = models.CharField(max_length=400, null=True, blank=True)
    instructions3 = models.CharField(max_length=400, null=True, blank=True)
    instructions4 = models.CharField(max_length=400, null=True, blank=True)
    instructions5 = models.CharField(max_length=400, null=True, blank=True)
    instructions6 = models.CharField(max_length=400, null=True, blank=True)
    instructions7 = models.CharField(max_length=400, null=True, blank=True)

    # production
    image = models.ImageField(default='default_image.jpg')


    def __str__(self):
        return self.name


class SavedRecipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)

class Comment(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

