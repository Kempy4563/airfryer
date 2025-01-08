# Generated by Django 5.1.4 on 2024-12-21 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "airfryer_app",
            "0008_alter_recipe_description_alter_recipe_ingredients1_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="recipe",
            name="user",
        ),
        migrations.AlterField(
            model_name="recipe",
            name="description",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients1",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients2",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients3",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients4",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="ingredients5",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions1",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions2",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions3",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions4",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="instructions5",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name="recipe",
            name="time",
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]