from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import AccommodationListing
from .serializers import AccommodationListingSerializer
from sites.models import Site


class AccommodationList(APIView):
    def get(self, request):
        # Get the site_id from the query params
        site_id = request.query_params.get('site_id')
        if site_id:
            # Filter accommodation listing by site
            site = Site.objects.get(pk=site_id)
            accommodation_listings = AccommodationListing.objects.filter(site=site)
        else:
            # Return an error if no site_id is provided
            return Response({"error": "site_id paramater is required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AccommodationListingSerializer(accommodation_listings, many=True)
        return Response(serializer.data)
