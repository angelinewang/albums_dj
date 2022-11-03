from django.shortcuts import render
from django.http import JsonResponse
from .models import Album
from django.views.generic import ListView
from rest_framework import generics
from .serializers import AlbumSerializer
# Create your views here.

def get_album(request):
    return JsonResponse({'name': 'Beat it!', 'artist': 'Michael Jackson'})

class AlbumListView(ListView):
    model = Album
    template="album.list.html"

class CreateListView(generics.ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

class RUDView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
