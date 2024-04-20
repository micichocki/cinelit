# Generated by Django 5.0.3 on 2024-04-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_remove_film_actors_remove_film_directors'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='directors',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.director'),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'unique_together': {('first_name', 'last_name')},
            },
        ),
        migrations.AddField(
            model_name='film',
            name='actors',
            field=models.ManyToManyField(blank=True, related_name='films', to='films.actor'),
        ),
    ]