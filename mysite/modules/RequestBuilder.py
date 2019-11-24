'''
    This file is used to create requests to be sent to the IMDb database
    based on request type
'''

import Request
class SearchRequest(Request.RequestHandler):
    def __init__(self, title = "", year = None):
        # Call to parent class
        super().__init__(title, year)
        
        # Which page to return out of 100
        self._page_num = 1 # Default page: 1, max: 100
    '''
        Setters for data controlled by url and
        specific to the SearchReqest class
    '''
    def setPageNum(self, numMoviesIn):
        self._page_num = numMoviesIn
        
    # Override parent function
    def makeRequest(self):
        # Build URL before making request
        self._build_search_url()
        
        # Make request by calling parent function
        super().makeRequest()
    
    def _build_search_url(self):
        if self._title != "":
            self.url = "%s&s=%s" % (self.url, self._title)
        if self._year != None:
            self.url = "%s&y=%d" % (self.url, self._year)
        if self._search_type != "":
            #append search type to each url
            self.url = "%s&type=%s" % (self.url, self._search_type)

        # append page number to each url
        self.url = "%s&page=%d" % (self.url, self._page_num)
        
class MovieRequest(Request.RequestHandler):
    def __init__(self, title = "", year = None):
        # Call to parent class
        super().__init__(title, year)
        
        self._movieID = ""
        self._plot_type = ""

    '''
        Setters for attributes added to url request and
        are specific to the MovieRequest class
    '''
    def setMovieId(self, mId):
        self._movieID = mId
    def setPlotType(self, plotType):
        # Plot type can be: short, full
        self._plot_type = plotType

    # Override parent method
    def makeRequest(self):
        # Build URL before making the request
        self._build_movie_url()
        
        # Make request by calling parent function
        super().makeRequest()
            
    def _build_movie_url(self):

        if self._title != "":
            self.url = "%s&t=*%s" % (self.url, self._title)
        if self._movieID != "":
            self.url = "%s&i=%s" % (self.url, self._movieID)
        if self._year != None:
            self.url = "%s&y=%d" % (self.url, self._year)
        if self._search_type != "":
            self.url = "%s&type=%s" % (self.url, self._search_type)
        if self._plot_type != "":
            self.url = "%s&plot=%s" % (self.url, self._plot_type)

        print(self.url)
        

if __name__ == "__main__":
    searchReq = SearchRequest("Guardians")
    searchReq.makeRequest()

    for i in range(9):
        currRequest = MovieRequest()
        currRequest.setMovieId(searchReq.getId(i))
        currRequest.makeRequest()
