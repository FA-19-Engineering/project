from django.urls import path
from . import views

urlpatterns = [
    #
    path('movie_search', views.movie_search, name='movie-search'),
    path('movie_display', views.movie_display, name='movie-display'),
    path('save_movie', views.save_movie, name='save-movie')
]