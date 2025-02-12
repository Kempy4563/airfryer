from django.urls import path
from . import views
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path('recipe/<int:id>/', views.detail, name='recipe'),
    path('recipes/<pk>/edit/', views.edit_recipe, name='edit_recipe'),
    path('user/<str:username>/recipes/', views.user_recipes, name='user_recipes'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('recipes/<int:recipe_id>/save/', views.save_recipe, name='save_recipe'),
    path('saved_recipes/', views.saved_recipes, name='saved_recipes'),
    path("saved_recipe/<int:id>/delete/", views.delete_saved_recipe, name="delete_saved_recipe"),
    path('search/', views.search_recipes, name='search_recipes'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
