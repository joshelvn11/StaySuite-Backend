from django.db import models
from django.contrib.auth.models import User

CURRENCY_CHOICES = [
    ('USD', 'US Dollar'),
    ('EUR', 'Euro'),
    ('GBP', 'British Pound'),
    ('JPY', 'Japanese Yen'),
    ('AUD', 'Australian Dollar'),
    ('CAD', 'Canadian Dollar'),
    ('ZAR', 'South African Rand'),
]


class Site(models.Model):
    site_name = models.CharField(max_length=100)
    site_slug = models.SlugField(unique=True)
    site_subdomain = models.CharField(max_length=24)
    site_design = models.JSONField(editable=True)
    site_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default="USD")

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


class UserSiteJunction(models.Model):
    site = models.ForeignKey(Site, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
