from rest_framework import generics
from .models import Scraper
from .serializers import ScraperSerializer

# Create your views here.


class ListScraperResultsView(generics.ListCreateAPIView):
    queryset = Scraper.objects.all()
    serializer_class = ScraperSerializer
