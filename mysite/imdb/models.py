# Imports
import sys

# set system path to allow Python to find Request Module
sys.path.append("modules/")

# Include RequestBuilder in current proejct
from RequestBuilder import MovieRequest, SearchRequest

# Create your models here.
# This is where requests will be made via Request.py in modules
class MovieModel:
    def __init__(self, movieTitle):
        searchReq = SearchRequest(movieTitle)
        searchReq.makeRequest()

        self._movies = []
        for i in range(9):
            currRequest = MovieRequest()
            currRequest.setMovieId(searchReq.getId(i))
            currRequest.makeRequest()
            
            currObj = {
                "title":currRequest.getTitle(),
                "year":currRequest.getYear(),
                "rated":currRequest.getRated(),
                "released":currRequest.getReleaseDate(),
                "runtime":currRequest.getRuntime(),
                 "plot":currRequest.getPlot()
            }
            self._movies.append(currObj)

    def getData(self):
        return self._movies
    
