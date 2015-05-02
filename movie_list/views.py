from django.shortcuts import render,get_object_or_404
from . models import Movie
from . forms import AddMovie

# Create your views here.
def movie_display(request):
	movies = Movie.objects.order_by('release_date')
	return render(request,'movie_list/movie_display.html',{'movies':movies})

def add_new(request):
	if request.method == 'POST':
		form = AddMovie(request.POST)
		if form.is_valid():
			post = form.save(commit= False)
			post.save()
	else:
		form = AddMovie()
	
	return render(request,'movie_list/add_movie.html',{'form': form})

def movie_detail(request,pk):
	movie = get_object_or_404(Movie,pk = pk)
	return render(request,'movie_list/movie_detail.html',{'movie':movie})