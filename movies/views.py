from django.shortcuts import render
from .models import Movies
from review.models import Reviews
from django.db.models import Avg 

# from movies.models import Movies
def movieview(request,slug):
    if Movies.objects.filter(slug=slug).exists():
        movie = Movies.objects.get(slug=slug) 
        if Reviews.objects.filter().exists():
            review = Reviews.objects.filter(movie=movie)
            no_users = review.count()
            rating = review.aggregate(avg_rating=Avg('rating')) 
        context = {
            'movie' : movie, 
            'rating' : rating['avg_rating'], 
            'no_users': no_users, 
            'reviews':review, 
        }
        return render(request, 'movies/movie_detail.html', context) 
    return render(request, 'movies/404.html', status=404) 

def movie_list(request): 
    language = request.GET.get('language', '').strip()
    genre = request.GET.get('genre', '').strip()

    movies = Movies.objects.all()
    if language:
        movies = movies.filter(language__iexact=language)
    if genre:
        movies = movies.filter(genre__iexact=genre)

    languages = ['English', 'Hindi', 'Telugu', 'Kannada', 'Tamil']
    genres = ['Action', 'Drama', 'Comedy', 'Thriller', 'Fantasy', 'Horror', 'Romance']

    context = {
        'movies': movies,
        'selected_language': language,
        'selected_genre': genre,
        'languages': languages,
        'genres': genres
    }
    return render(request, 'movies/filter.html', context) 