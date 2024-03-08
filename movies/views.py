from django.shortcuts import render
import requests
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Movie
from .serializers import MovieSerializer

@api_view(['GET'])
def fetch_movies(request):
    url = 'https://catfact.ninja/fact?max_length=140'
    response = requests.get(url)
    stats = response.json()

    context = {
        'stats': stats
    }

    return render(request, 'movies/movie.html', context)
# dad71b10920ce2993bd44abf3489eb76