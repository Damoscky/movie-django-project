from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Movie


def movies(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movies.html', {'movies': movies})
    # return HttpResponse("Hello")


def index(request):
    return HttpResponse("Home Page")


def movie(request, id):
    data = Movie.objects.get(pk=id)
    return render(request, 'movies/details.html', {'movie': data})


def addMovies(request):
    return render(request, 'movies/add-movie.html')

def store(request):
    title = request.POST['title']
    year = request.POST['year']
    
    if title and year:
        movie = Movie(
            title=title,
            year=year
        )
        movie.save()
        return HttpResponseRedirect('/movies')

def delete(request, id):
    try:
        movie = Movie.objects.get(pk=id)
    except:
        raise Http404('Movie does not exist')
        
    movie.delete()
    return HttpResponseRedirect('/movies')

    