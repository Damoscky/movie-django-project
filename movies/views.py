from django.http import HttpResponse
from django.shortcuts import render

data = {
    'movies': [
        {
            'id': 4,
            'title': 'Jaws',
            'year': 1900
        },
        {
            'id': 5,
            'title': 'Mark',
            'year': 1630
        },
        {
            'id': 6,
            'title': 'Stephen',
            'year': 1830
        }
    ]
}
def movies(request):
    return render(request, 'movies/movies.html', data)
    # return HttpResponse("Hello")


def index(request):
    return HttpResponse("Home Page")