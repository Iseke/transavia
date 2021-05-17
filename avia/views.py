from django.shortcuts import render

from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from avia.serializers import SearchSerializer


class SearchView(generics.CreateAPIView):
    permission_classes = (AllowAny, )
    serializer_class = SearchSerializer

    def post(self, request, *args, **kwargs):
        search_field = request.data['code']
        print(search_field)
        return Response(status=status.HTTP_200_OK)