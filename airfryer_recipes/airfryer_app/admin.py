from django.contrib import admin
from .models import Recipe, Comment, SavedRecipe


admin.site.site_header = "Airfryer Recipes"
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(SavedRecipe)
