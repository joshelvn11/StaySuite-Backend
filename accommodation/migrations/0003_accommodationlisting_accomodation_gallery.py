# Generated by Django 4.2.10 on 2024-06-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0002_remove_sitesettings_site_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='accommodationlisting',
            name='accomodation_gallery',
            field=models.JSONField(null=True),
        ),
    ]