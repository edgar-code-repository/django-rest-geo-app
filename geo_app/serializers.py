from rest_framework import serializers

from .models import Continent, Country, City


class ContinentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Continent
        fields = ('id','name')


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('id','name', 'continent')


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'name', 'country')

