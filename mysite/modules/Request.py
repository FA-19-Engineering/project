'''
    The RequestHandler clsss handles the requests sent to it
    and stores data in the Request class

    To include in a project, must added folder/module
    to module path for python to search
    [
        ie.
        import sys
        sys.path.append("relative path")
    ]
'''
# imports
import sys

# Include module path for python to search
sys.path.append("dependencies/")

import requests
from Queries import MovieQuery, SearchQuery
'''
    The Request class is meant to handle the setters and getters
    for the URL request
'''
class Request:
    def __init__(self, title = "", year = None):
        self._title = title
        self._year = year
        self._search_type = "movie" # movie by default
    '''
        Setters and Getters for data controlled by url before
        request is made and is shared by all Requests
    '''
    # Setters
    def setTitle(self, title):
        self._title = title
    def setSearchType(self,srcType):
        # Search type can be: movie, series, episode
        self._search_type = srcType
    def setYear(self, yIn):
        self._year = yIn

    # Store type of query
    def storeQuery(self, jsonData):
        if (self.__class__.__name__ == "MovieRequest"):
            self._query = MovieQuery(jsonData)
        elif (self.__class__.__name__ == "SearchRequest"):
            self._queries:SearchQuery = {}
            
            for i in range(len(jsonData["Search"])):
                currMovie = jsonData["Search"][i]
                
                self._queries[i] = SearchQuery(currMovie)
                
    '''
        Getters for data after request
        has been made
    '''
    def getTitle(self, movieNum=0):
        if self.__class__.__name__ == "MovieRequest":
            return self._query.getTitle()
        else: # Search Request => Requires movie number for return json
            return self._queries[movieNum].getTitle()
        
    def getYear(self, movieNum=0):
        if self.__class__.__name__ == "MovieRequest":
            return self._query.getYear()
        else: # Search Request => Requires movie number for return json
            return self._queries[movieNum].getYear()
        
    def getPosterURL(self, movieNum=0):
        if self.__class__.__name__ == "MovieRequest":
            return self._query.getPosterURL()
        else: # Search Request => Requires movie number for return json
            return self._queries[movieNum].getPosterURL()

    def getId(self, movieNum=0):
        if self.__class__.__name__ == "MovieRequest":
            return self._query.getId()
        else: # Search Request => Requires movie number for return json
            return self._queries[movieNum].getId()
    def getRated(self):
        return self._query.getRated()
    def getReleaseDate(self):
        return self._query.getReleaseDate()
    def getRuntime(self):
        return self._query.getRuntime()
    def getGenre(self):
        return self._query.getGenre()
    def getPlot(self):
        return self._query.getPlot()
    
    
'''
    The RequestHandler class handles the functionality and sending of request
    to IMDb database
'''
class RequestHandler(Request):
    _api = "84e37cb7"
    _domain = "http://www.omdbapi.com/?"

    def __init__(self, title = "", year = None):
        super().__init__(title, year)
        
        self._json = ""
        self._search_type = ""

        # Create base of url for all IMDb requests
        self.url = RequestHandler._domain + "apikey=" + RequestHandler._api
        
    def makeRequest(self):
        # Make request to current url
        # Send request
        response = requests.get(self.url)
        if (response.status_code == 200):
            self._json = response.json()
            if (response.json()["Response"] == 'True'):
                self.storeQuery(self._json)
            else:
                print("Unable to find Request")
        elif response.status_code == 404:
            print("Unable to return resource")
        else:
            print(response.status_code)
