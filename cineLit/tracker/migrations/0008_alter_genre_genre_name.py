# Generated by Django 5.0.3 on 2024-05-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0007_alter_userstat_average_reading_speed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_name',
            field=models.CharField(max_length=255),
        ),
    ]
