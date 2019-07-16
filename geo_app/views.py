from rest_framework import viewsets

from .models import Continent, Country, City
from .serializers import ContinentSerializer, CountrySerializer, CitySerializer


class ContinentView(viewsets.ModelViewSet):
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer

class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer

class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer

