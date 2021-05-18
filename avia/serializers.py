from rest_framework import serializers

from .models import City, Airport, Country


class SearchSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)


class CountrySerializer(serializers.ModelSerializer):

    class Meta:
        model = Country
        fields = ['country_code', 'country_name']


class CitySerializer(serializers.ModelSerializer):
    # country_code = CountrySerializer

    class Meta:
        model = City
        fields = ['city_code', 'city_name']


class AirportSerializer(serializers.ModelSerializer):
    # country_code = CountrySerializer
    # city_code = CitySerializer

    class Meta:
        model = Airport
        fields = ['airport_code', 'airport_name']