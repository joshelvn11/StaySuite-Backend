from django.db import models
from sites.models import Site

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
