from django.urls import path
from . import views

urlpatterns = [
  
    path('Theater_show_time/<slug:slug>/', views.Theatre_show_time, name='show_time'),
    path('showtimes/<slug:slug>/<date_str>/', views.theater_show_time_selected_date_view, name='theater_showtime_date'),
    path('seat_selection/<int:showtime_id>/', views.seat_selection_view, name='seat_selection'),
]
