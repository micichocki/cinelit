# Generated by Django 5.0.3 on 2024-05-25 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_alter_book_cover'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='author',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
