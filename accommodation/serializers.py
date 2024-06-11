from rest_framework import serializers
from .models import AccommodationListing


class AccommodationListingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccommodationListing
        fields = [
            'id', 'site', 'accommodation_name', 'accommodation_slug',
            'accommodation_type', 'accommodation_price_type',
            'accomodation_price', 'accommodation_description',
            'accommodation_excerpt', 'accommodation_gallery',
        ]
