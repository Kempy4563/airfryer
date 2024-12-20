from django.shortcuts import render
from .models import Recipe


def index(request):
    recipes = Recipe.objects.all()
    return render(request, "airfryer_app/index.html", {"recipes": recipes})

def detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    return render(request, "airfryer_app/detail.html", {"recipe": recipe})

