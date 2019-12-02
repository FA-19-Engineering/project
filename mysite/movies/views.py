from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Movie
from .forms import SearchForm
from .search import movieRequest
# Create your views here.

#home view returns the basic search page of the app
#the search form is brought in here
@login_required
def movie_search(request):
    form = SearchForm()
    context = { "form": form }
    return render(request, "movie_search.html", context)

#display view 
@login_required
def movie_display(request):
    if request.method == 'GET':
        form = SearchForm(request.GET)

        if form.is_valid():
            searchVal = form.cleaned_data.get('query', '')

        # moviesData is a list containing the (usually) 10 Movies
        # returned by a user's search. 
        moviesData = movieRequest(form)
        return render(request, 'movie_display.html', {'movies': moviesData})
