# Generated by Django 4.2.10 on 2024-06-06 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='site_slug',
            field=models.SlugField(unique=True),
        ),
    ]
