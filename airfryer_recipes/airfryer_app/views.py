from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment
from .forms import RecipeForm, CommentForm
from .models import SavedRecipe



def index(request):
    recipes = Recipe.objects.all()
    return render(request, "airfryer_app/index.html", {"recipes": recipes})


def detail(request, id):
    recipe = Recipe.objects.get(pk=id)
    print(recipe.instructions1)
    print(recipe.instructions2)
    print(recipe.instructions3)
    print(recipe.instructions4)
    print(recipe.instructions5)
    print(recipe.instructions6)
    print(recipe.instructions7)
    is_saved = False
    if request.user.is_authenticated:
        is_saved = SavedRecipe.objects.filter(user=request.user, recipe=recipe).exists()

    comments = Comment.objects.filter(recipe=recipe)

    comment_form = CommentForm()

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.user = request.user
            comment.save()
            return redirect('recipe', id=id)
        else:
            print(comment_form.errors)  # Print out the form errors
    else:
        form = RecipeForm(instance=recipe)

    return render(request, "airfryer_app/detail.html", {"recipe": recipe, "form": form, "is_saved": is_saved, "comments": comments, "comment_form": comment_form})


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
        return redirect('recipe_detail', pk=pk)


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


@login_required
def save_recipe(request, recipe_id):
    recipe = Recipe.objects.get(id=recipe_id)
    saved_recipe, created = SavedRecipe.objects.get_or_create(user=request.user, recipe=recipe)

    return redirect('recipe', id=recipe_id)


def saved_recipes(request):
    user_saved_recipes = SavedRecipe.objects.filter(user=request.user)
    return render(request, 'airfryer_app/saved_user_recipes.html', {'user_saved_recipes': user_saved_recipes})


def delete_saved_recipe(request, id):
    saved_recipe = SavedRecipe.objects.get(id=id)
    saved_recipe.delete()
    return redirect("saved_recipes")

def search_recipes(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        print("Query:", query)
        recipes = Recipe.objects.filter(name__icontains=query)
        print("Recipes:", recipes)
        return render(request, 'airfryer_app/search_results.html', {'recipes': recipes})



