# Generated by Django 4.2.5 on 2023-11-09 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender_app', '0007_liked_recipes_date_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked_recipes',
            name='date_liked',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]