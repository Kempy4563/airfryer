from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe
from .forms import RecipeForm




def index(request):
    recipes = Recipe.objects.all()
    return render(request, "airfryer_app/index.html", {"recipes": recipes})

def detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    if request.method == 'POST':
        if request.user == recipe.user:
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('detail', id=id)
        else:
            return redirect('detail', id=id)
    else:
        form = RecipeForm(instance=recipe)
    return render(request, "airfryer_app/detail.html", {"recipe": recipe, "form": form})

@login_required
def edit_recipe(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.user == recipe.user:
        if request.method == 'POST':
            form = RecipeForm(request.POST, instance=recipe)
            if form.is_valid():
                form.save()
                return redirect('recipe', id=pk)
        else:
            form = RecipeForm(instance=recipe)
        return render(request, 'airfryer_app/edit_recipe.html', {'form': form})
    else:
        return redirect('detail', pk=pk)

@login_required
def user_recipes(request, username):
    user = get_object_or_404(User, username=username)
    recipes = Recipe.objects.filter(user=user)
    return render(request, 'airfryer_app/user_recipes.html', {'recipes': recipes})

@login_required
def add_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('user_recipes', request.user.username)
    else:
        form = RecipeForm()
    return render(request, 'airfryer_app/add_recipe.html', {'form': form})

