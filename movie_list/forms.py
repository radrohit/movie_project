from django import forms
from .models import Movie


class AddMovie(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ['movie_name', 'release_date', 'movie_poster',
                  'movie_description', 'mpaa_rating', 'imdb_rating', 'genre_id']
