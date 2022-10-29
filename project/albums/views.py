from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def get_album(request):
    return JsonResponse({'name': 'Beat it!', 'artist': 'Michael Jackson'})
