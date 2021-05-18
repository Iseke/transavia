from .models import City, Airport
from .serializers import AirportSerializer, CitySerializer


def search_city(substring):
    if len(substring) == 3:
        cities = City.objects.filter(city_code__icontains=substring)

        if cities:
            res = city_airports(cities)
            return res
    cities = City.objects.filter(city_name__icontains=substring)
    if cities:
        res = city_airports(cities)
        return res
    if len(substring) == 3:
        airports = Airport.objects.filter(airport_code__icontains=substring)
        if airports:
            res = airport_city(airports)
            return res
    airports = Airport.objects.filter(airport_name__icontains=substring)
    if airports:
        res = airport_city(airports)
        return res
    return False


def city_airports(cities):
    res = []
    for city in cities:
        cur_airports = city.airport_city
        airport_serializer = AirportSerializer(cur_airports, many=True)
        city_serializer = CitySerializer(city)

        res.append({
            'city': city_serializer.data,
            'airports': airport_serializer.data
        })
    return res


def airport_city(airport):
    res = []
    for air in airport:
        res.append(air.to_json())
    return res
