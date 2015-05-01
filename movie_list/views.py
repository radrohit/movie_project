from django.shortcuts import render
from . models import Movie

# Create your views here.
def movie_display(request):
	movies = Movie.objects.order_by('release_date')
	return render(request,'movie_list/movie_display.html',{'movies':movies})

