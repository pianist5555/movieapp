from django.core.management.base import BaseCommand, CommandError
from movieapp.models import * 
import requests

class Command(BaseCommand):
    def handle(self, *args, **options):
        url = "https://yts.mx/api/v2/list_movies.json?limit=50"
        response = requests.get(url)
        movie_data = response.json().get('data').get('movies')
        for md in movie_data:
            movie = Movie()
            movie.title = md['title']
            movie.year = md['year']
            movie.summary = md['summary']
            movie.rating = md['rating']

            genre_appended = ''
            for genre in md['genres']:
                genre_appended +=  genre + ' '

            movie.genres = genre_appended
            movie.save()
