from django.urls import path

from . import views

urlpatterns = [
    # Regexp for finding an expression that has one or more word characters
    #  found at the end of the url string following the imdb/ url string
    #path('', views.movie_search),
    path('movie_search/', views.movie_search, name="movie-search"),
    path('movie_display/', views.movie_display, name="movie-display")
]
