from django.http import Http404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import SiteSerializer
from .models import Site


class SiteDetail(APIView):
    serializer_class = SiteSerializer

    def get_object(self, slug):
        try:
            site = Site.objects.get(site_slug=slug)
            return site
        except Site.DoesNotExist:
            raise Http404

    def get(self, request, slug):
        site = self.get_object(slug)
        serializer = SiteSerializer(site)
        return Response(serializer.data)

    def put(self, request, slug):
        site = self.get_object(slug)
        serializer = SiteSerializer(site, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
