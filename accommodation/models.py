from django.db import models
from django.contrib.auth.models import User

CURRENCY_CHOICES = [
        ('USD', 'US Dollar'),
        ('EUR', 'Euro'),
        ('GBP', 'British Pound'),
        ('JPY', 'Japanese Yen'),
        ('AUD', 'Australian Dollar'),
        ('CAD', 'Canadian Dollar'),
        ('CHF', 'Swiss Franc'),
        ('CNY', 'Chinese Yuan'),
        ('INR', 'Indian Rupee'),
        ('RUB', 'Russian Ruble'),
        ('BRL', 'Brazilian Real'),
        ('ZAR', 'South African Rand'),
        ('MXN', 'Mexican Peso'),
        ('SGD', 'Singapore Dollar'),
        ('HKD', 'Hong Kong Dollar'),
        ('NZD', 'New Zealand Dollar'),
        ('SEK', 'Swedish Krona'),
        ('NOK', 'Norwegian Krone'),
        ('DKK', 'Danish Krone'),
        ('PLN', 'Polish Zloty'),
        ('THB', 'Thai Baht'),
        ('MYR', 'Malaysian Ringgit'),
        ('IDR', 'Indonesian Rupiah'),
        ('PHP', 'Philippine Peso'),
        ('VND', 'Vietnamese Dong'),
        ('KRW', 'South Korean Won'),
        ('AED', 'United Arab Emirates Dirham'),
        ('SAR', 'Saudi Riyal'),
        ('TRY', 'Turkish Lira'),
    ]

ACCOMMODATION_TYPES = [
        (0, "Home"),
        (1, "Room"),
        (2, "Camping Site")
    ]

ACCOMMODATION_PRICE_TYPES = [
        (0, "Per Night"),
        (1, "Per Person Per Night"),
        (2, "Per Week"),
        (3, "Per Month"),
    ]


class Site(models.Model):
    site_name = models.CharField(max_length=100)
    site_slug = models.SlugField()
    site_subdomain = models.CharField(max_length=24)
    site_design = models.JSONField(editable=True)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Sites"

    def __str__(self):
        return f"{self.site_name}"


class SiteSettings(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)

    class Meta:
        verbose_name = "Site Settings"
        verbose_name_plural = "Site Settings"

    def __str__(self):
        return f"{self.site.site_name} Settings"


class AccommodationListing(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE)
    accommodation_name = models.CharField(max_length=100)
    accommodation_slug = models.SlugField(max_length=50)
    accommodation_type = models.IntegerField(choices=ACCOMMODATION_TYPES)
    accommodation_price_type = models.IntegerField(choices=ACCOMMODATION_PRICE_TYPES)
    accomodation_price = models.IntegerField()
    accommodation_description = models.TextField()
    accommodation_excerpt = models.TextField()

    class Meta:
        verbose_name = "Accommodation Listing"
        verbose_name_plural = "Accommodation Listings"

    def __str__(self):
        return f"{self.accommodation_name} | {self.site.site_name}"


class UserSiteJunction(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
