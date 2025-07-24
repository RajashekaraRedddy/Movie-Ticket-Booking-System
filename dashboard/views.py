from django.shortcuts import render
from movies.models import Movies

# Create your views here.
def movie_listview(request):
    context = {
        'movies': Movies.objects.all()
    }
    return render(request, 'movies/movies.html', context)  