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
        slug = request.query_params.get('slug')
        if slug:
            # Filter accommodation listing by site
            site = Site.objects.get(site_slug=slug)
            accommodation_listings = AccommodationListing.objects.filter(site=site)
        else:
            # Return an error if no site_id is provided
            return Response({"error": "site_id paramater is required"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AccommodationListingSerializer(accommodation_listings, many=True)
        return Response(serializer.data)


class AccommodationDetail(APIView):

    serializer_class = AccommodationListingSerializer

    def get_object(self, accom_slug):
        try:
            accommodation = AccommodationListing.objects.get(accommodation_slug=accom_slug)
            return accommodation
        except AccommodationListing.DoesNotExist:
            raise Http404

    def get(self, request, accom_slug):
        accommodation = self.get_object(accom_slug)
        serializer = AccommodationListingSerializer(accommodation)
        return Response(serializer.data)
