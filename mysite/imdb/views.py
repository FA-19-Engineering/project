from django.shortcuts import render
from django.contrib.auth.decorators import login_required

import sys
sys.path.append("imdb/")
# include model to handle Movie Requests
from models import MovieModel

# Create your views here.
@login_required
def home(request):
    return render(request, "movie_display.html", {"searchResult": movie_list,"userSearch":"Guardians"})#genreData.getData()})

@login_required
def movie_search(request):
    return render(request, "movie_search.html")

@login_required
def movie_display(request):
    userInput = request.GET['searchVal']
    requestInfo = MovieModel(userInput)
    
    return render(request, "movie_display.html", {"searchResult": requestInfo.getData(),"userSearch":userInput})

