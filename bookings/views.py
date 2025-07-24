from django.shortcuts import render
from theater.models import Theatre, Showtimes
from movies.models import Movies
from datetime import datetime, timedelta
from theater.models import *

# Create your views here.
def Theatre_show_time(request, slug):
    today = datetime.today().date()
    
    start_date = today
    week = [{
        'name': (start_date + timedelta(days=i)).strftime("%a").upper(),
        'day': (start_date + timedelta(days=i)).day,
        'month': (start_date + timedelta(days=i)).strftime("%b").upper(),
        'date': start_date + timedelta(days=i),
        'slug': slug,
    } for i in range(7)] 
    try:
        movie = Movies.objects.get(slug=slug)
        theater_showtimes = [
            Showtimes.objects.filter(movie=movie, theater=theatre).order_by('show_time')
            for theatre in Theatre.objects.all() if Showtimes.objects.filter(movie=movie, theater=theatre).exists()
        ]
        context = {
            'theater_showtimes': theater_showtimes,
            'week': week,
            'today': today,
            'slug': slug,  
        }
        return render(request, 'theater/theater_showtimes_list.html', context)
    except Movies.DoesNotExist:
        return render(request, 'movies/404.html')

def theater_show_time_selected_date_view(request, slug, date_str):
    try:
      
        selected_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError:
        selected_date = datetime.today().date()

    today = datetime.today().date()
    start_date = today
    
    week = [{
        'name': (start_date + timedelta(days=i)).strftime('%a').upper(),
        'day': (start_date + timedelta(days=i)).day,
        'month': (start_date + timedelta(days=i)).strftime('%b').upper(),
        'date': start_date + timedelta(days=i), 
    } for i in range(7)]

    
    try:
        movie = Movies.objects.get(slug=slug)
        theater_showtimes = [
            Showtimes.objects.filter(movie=movie, theater=theater, show_time__date=selected_date).order_by('show_time')
            for theater in Theatre.objects.all() if Showtimes.objects.filter(movie=movie, theater=theater, show_time__date=selected_date).exists()
        ]
        context = {
            'theater_showtimes': theater_showtimes,
            'week': week,
            'today': selected_date,
            'slug': slug,
        }
        return render(request, 'theater/theater_showtimes_list.html', context)
    except Movies.DoesNotExist:
        return render(request, 'movies/404.html')


def seat_selection_view(request,showtime_id):
    showtime = Showtimes.objects.get(id = showtime_id)
    all_seats = Seats.objects.filter(
        theater = showtime.theater,
        screen_number = showtime.screen_number
    ).order_by('row_label', 'seat_number')


    seat_rows = { 'A':[1,2,3,4,5,6,7,8,9,10],
                    'B':[1,2,3,4,5,6,7,8,9,10],
                    'C':[1,2,3,4,5,6,7,8,9,10],
                    'D':[1,2,3,4,5,6,7,8,9,10],
                    'E':[1,2,3,4,5,6,7,8,9,10],
                    'F':[1,2,3,4,5,6,7,8,9,10],
                    'G':[1,2,3,4,5,6,7,8,9,10],
                    'H':[1,2,3,4,5,6,7,8,9,10],} 
    for seat in all_seats:
        row = seat.row_label
        if row not in seat_rows: 
            seat_rows[row] = []
        seat_rows[row].append(seat)

    context = {
        'showtime' : showtime,
        'seat_rows' : seat_rows,
    }
    return render(request, 'theater/seating.html',context) 