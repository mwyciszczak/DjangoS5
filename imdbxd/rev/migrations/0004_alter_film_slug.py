# Generated by Django 4.1.3 on 2022-11-18 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rev', '0003_alter_film_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='slug',
            field=models.SlugField(editable=False, max_length=150, null=True),
        ),
    ]
