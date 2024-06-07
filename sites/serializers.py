from rest_framework import serializers
from .models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = [
            'id', 'site_name', 'site_slug', 'site_subdomain', 'site_design',
        ]
