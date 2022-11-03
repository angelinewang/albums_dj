from django.shortcuts import render
from django.http import JsonResponse
from .models import Artist
from django.views.generic import ListView
from rest_framework import generics
from .serializers import ArtistSerializer
# Create your views here.


def get_artist(request):
    return JsonResponse({'name': "Taylor Swift"})

class ArtistsListView(ListView):
    model = Artist
    template = "artist.list.html"

class CreateListView(generics.ListCreateAPIView):
    queryset = Artist.objects.all()
    serializer_class = ArtistSerializer
