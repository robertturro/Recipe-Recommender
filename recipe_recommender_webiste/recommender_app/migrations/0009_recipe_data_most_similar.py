# Generated by Django 4.2.5 on 2023-11-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_app', '0008_alter_liked_recipes_date_liked'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe_data',
            name='most_similar',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
