from django.db import models
from django.contrib.auth.models import *
from django.conf import settings

# the movie model will store a movie type object
# which contains a few details and a link to the user who saves it.
class Movie(models.Model):
    title = models.CharField(max_length = 200) #longest title I found was 197
    mID = models.CharField(max_length = 50)
    year = models.CharField(max_length = 6, default = '5555')
    posterURL = models.CharField(max_length = 250, default = 'https://m.media-amazon.com/images/M/MV5BNWM4M2QwOWUtNGMwMS00Nzg2LTg0YjktYTU4M2ZhYTMwYTU5XkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_UX182_CR0,0,182,268_AL_.jpg')
    # user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # ^^EXPERIMENTAL

    # have self function just return the movie ID
    def __str__(self):
        return f"{self.title} - {self.mID}"

    