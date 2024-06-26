# Generated by Django 4.2.10 on 2024-06-07 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_alter_site_site_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='site',
            name='site_currency',
            field=models.CharField(choices=[('USD', 'US Dollar'), ('EUR', 'Euro'), ('GBP', 'British Pound'), ('JPY', 'Japanese Yen'), ('AUD', 'Australian Dollar'), ('CAD', 'Canadian Dollar'), ('CHF', 'Swiss Franc'), ('CNY', 'Chinese Yuan'), ('INR', 'Indian Rupee'), ('RUB', 'Russian Ruble'), ('BRL', 'Brazilian Real'), ('ZAR', 'South African Rand'), ('MXN', 'Mexican Peso'), ('SGD', 'Singapore Dollar'), ('HKD', 'Hong Kong Dollar'), ('NZD', 'New Zealand Dollar'), ('SEK', 'Swedish Krona'), ('NOK', 'Norwegian Krone'), ('DKK', 'Danish Krone'), ('PLN', 'Polish Zloty'), ('THB', 'Thai Baht'), ('MYR', 'Malaysian Ringgit'), ('IDR', 'Indonesian Rupiah'), ('PHP', 'Philippine Peso'), ('VND', 'Vietnamese Dong'), ('KRW', 'South Korean Won'), ('AED', 'United Arab Emirates Dirham'), ('SAR', 'Saudi Riyal'), ('TRY', 'Turkish Lira')], default='USD', max_length=3),
        ),
    ]
