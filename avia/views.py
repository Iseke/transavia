import redis
import json

from django.conf import settings

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from avia.models import City, Airport
from avia.serializers import SearchSerializer, CitySerializer
from avia.utils import search_city

redis_instance = redis.Redis(host=settings.REDIS_HOST,
                             port=int(settings.REDIS_PORT))


class SearchView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = SearchSerializer
    queryset = Airport.objects.all()

    def create(self, request, *args, **kwargs):
        search_field = request.data['code']
        if redis_instance.get(search_field):
            rare_data = redis_instance.get(search_field)
            res = json.loads(rare_data.decode())
            return Response(data=res, status=status.HTTP_200_OK)
        res = search_city(substring=search_field)
        if res:
            redis_instance.set(search_field, json.dumps(res))
            return Response(data=res, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)
