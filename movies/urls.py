from django.urls import path
from . import views

urlpatterns = [
    path('movie/<slug>/',views.movieview,name='movie'),
    path('filter/', views.movie_list, name='filter'), 

] 