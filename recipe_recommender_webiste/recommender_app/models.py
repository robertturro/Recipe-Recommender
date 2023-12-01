from django.db import models
from import_export import resources 

class Liked_Recipes(models.Model):
    recipe = models.CharField(max_length=50,primary_key=True)
    user = models.CharField(max_length=30)
    recipe_name = models.CharField(max_length=30,null=True,blank=True)
    description = models.CharField(max_length=500,null=True,blank=True)
    ingredients = models.CharField(max_length=300,null=True,blank=True)
    steps = models.CharField(max_length=300,null=True,blank=True)
    calories = models.FloatField(null=True,blank=True)
    protein = models.FloatField(null=True,blank=True)
    carbs = models.FloatField(null=True,blank=True)
    sugar = models.FloatField(null=True,blank=True)
    time = models.IntegerField(null=True,blank=True)
    tag_bins = models.CharField(max_length=1000,null=True,blank=True)
    ingredients_bin = models.CharField(max_length=1000,null=True,blank=True)
    date_liked = models.DateTimeField(null=True,blank=True)


class Recipe_Data(models.Model):
    recipe = models.IntegerField(primary_key=True)
    tags = models.CharField(max_length=1000,null=True,blank=True)
    nutrition = models.CharField(max_length=50,null=True,blank=True)
    minutes = models.IntegerField(null=True,blank=True)
    ingredients = models.CharField(max_length=1000,null=True,blank=True)
    ethnicity = models.CharField(max_length=30,null=True,blank=True)
    type_of_food = models.CharField(max_length=30,null=True,blank=True)
    holiday = models.CharField(max_length=30,null=True,blank=True)
    dietary_restriction = models.CharField(max_length=30,null=True,blank=True)
    ingredients_bin = models.CharField(max_length=1000,null=True,blank=True)
    calories = models.FloatField(null=True,blank=True)
    sugar = models.FloatField(null=True,blank=True)
    protein = models.FloatField(null=True,blank=True)
    carbs = models.FloatField(null=True,blank=True)
    recipe_name = models.CharField(max_length=100,null=True,blank=True)
    recipe_steps = models.CharField(max_length=300,null=True,blank=True)
    description = models.CharField(max_length=1000,null=True,blank=True)
    ingredients_html = models.CharField(max_length=1000,null=True,blank=True)
    steps_html = models.CharField(max_length=1000,null=True,blank=True)
    description_html = models.CharField(max_length=1000,null=True,blank=True)
    recipe_name_html = models.CharField(max_length=1000,null=True,blank=True)
    tag_bins = models.CharField(max_length=1000,null=True,blank=True)
    most_similar = models.IntegerField(null=True,blank=True)



