# Generated by Django 4.2.5 on 2023-11-08 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_app', '0003_alter_recipe_data_calories_alter_recipe_data_carbs_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_recipes',
            name='calories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='carbs',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='ingredients',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='protein',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='recipe_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='steps',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='sugar',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='liked_recipes',
            name='time',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]