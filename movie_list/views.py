from django.shortcuts import render, get_object_or_404, redirect
import re
from . models import Movie
from . forms import AddMovie


# Create your views here.


def movie_display(request):
    movies = Movie.objects.order_by('release_date')
    return render(request, 'movie_list/movie_display.html', {'movies': movies})


def add_new(request):
    if request.method == 'POST':
        form = AddMovie(request.POST)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_list.views.movie_detail', pk=post.pk)
    else:
        form = AddMovie()

    return render(request, 'movie_list/add_movie.html', {'form': form})


def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_list/movie_detail.html', {'movie': movie})


def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == 'POST':
        form = AddMovie(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save(commit=False)
            movie.save()
            return redirect('movie_list.views.movie_detail', pk=movie.pk)
    else:
        form = AddMovie(instance=movie)
    return render(request, 'movie_list/movie_edit.html', {'form': form})


def search_result(request):
    result = []
    if 'q' in request.GET:
        term = request.GET['q']
        for movie in Movie.objects.all():
            if re.search(term, movie.movie_name):
                result.append(movie)
    else:
        result = movie_list.objects.all()

    return render(request, 'movie_list/search_result.html', {'result': result})
