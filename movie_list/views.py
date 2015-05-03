from django.shortcuts import render, get_object_or_404, redirect
import re
from . models import Movie
from . forms import AddMovie


# Create your views here.


def movie_display(request):
    """
    arguments:
    request: a http request

    variables:
    movies: contains movie object in descending order of release date 

    Returns:
    renders movie_display.html page with the movie object

    This function takes a http request and creates the html page with the
    movie object.  


    """
    movies = Movie.objects.order_by('-release_date')
    return render(request, 'movie_list/movie_display.html', {'movies': movies})


def add_new(request):
    """
    arguments:
    request: a http request

    variables:
    form: django AddMovie form object that is created in class forms.py

    Returns:
    dispalys add_movie.html page with the form object

    when we save our form the http POST request is made and during regular
    lookup GET request is made. If the request is GET we display the html page
    with the form. If the request is POST and all the entries in the form are
    valid we redirect to the movie details page while saving the details in database. If the form 
    is not valid we display the form and allowing the user to reedit the values

    """

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
    """
    arguments:
    request: a http request
    pk: primary key from movie

    variables:
    movie: if primary key is in Movie return a particular movie else
       return 404 not found page 

    Returns:
    displays movie_detail.html page with the movie object

    This function takes a http request and pk and looksup the primary key
    in Movie database and return the details of particular. The response movie_detail
    and movie variable are rendered in the browser.


    """
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movie_list/movie_detail.html', {'movie': movie})


def movie_edit(request, pk):
    """
    arguments:
    request: a http request
    pk: primary key from movie 

    variables:
    movie: if primary key is in Movie return a particular movie else
       return 404 not found page 
    form: django AddMovie form object that is created in class forms.py
       and inadditon we pass in movie object to be edited.

    Returns:
    A movie_edit.html page with the form filled with contents from movie object

    when we save our form the http POST request is made and during regular
    lookup GET request is made. If the request is GET we display the html page
    with the form prefilled with movie object. If the request is POST and 
    all the entries in the form are valid we redirect to the movie details page while saving 
    the form in database. If the form is not valid we display the form 
    and allowing the user to reedit the values


    """
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
    """
    arguments:
    request: a http request

    variables:
    result: stores the search results
    term: search term

    Returns:
    displays search_result.html page with the search results

    This function takes a http request and uses regular expression to 
    match the syntax


    """

    result = []
    if 'q' in request.GET:
        term = request.GET['q']
        for movie in Movie.objects.all():
            if re.search(term, movie.movie_name,re.IGNORECASE):
                result.append(movie)

    return render(request, 'movie_list/search_result.html', {'result': result})
