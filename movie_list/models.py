from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import datetime
import os


# Create your models here.
class Genre(models.Model):

    """This class is used for Genre and is declared to create a
    many to many relationship with the class Movie.

    This class inherits from models.Model which is provided by Django and
    allows user to create fields in database specified in settings.py.
    Attributes:
        genre_name: Title field for genre of a movie. example: Comedy and
           Action
        genre_description: Field that gives a short description of the genre

    """
    genre_name = models.CharField(max_length=100)
    genre_description = models.TextField(max_length=300, blank=True)

    def __str__(self):
        """
        Returns the human readable representation of the object which in this
        case is genre title. 

        """
        return self.genre_name

class Movie(models.Model):

    """This is main model for our movie website and it is used to create
    primary database table of the project. 

    This class inherits from models.Model which is provided by Django and
    allows user to create fields in database specified in settings.py. The
    django migration runs sql queris to create database and table.

    Attributes:
       MPAA_RATINGS: Ratings based on MPAA website that gives viewer
          discretion. This is assigned to variable mpaa_rating where the 
          tuple of tuple allows to easily create a drop down list.
       movie_name: Title of movie. 
       release_date: Movie release year. Allows only years from 1880 to 
          2100 and default year is current year. 
       movie_poster: Movie thumbnail. Allows user to upload image 
          from their devices. Django for efficiency has link to the 
          image and does not store actual image.
       movie_description: Description of movie. Not mandatory.
       imdb_rating: IMDB website rating and allows only value from 0
          to 10.
       genre_id: Genre of movie. Has to many to many relationship
          with Genre table.

    """

    MPAA_RATINGS = (
        ('G', 'G'),
        ('PG', 'PG'),
        ('PG-13', 'PG-13'),
        ('R', 'R'),
        ('NC-17', "NC-17"),
        ('N/A', "Not Available"),
    )
    movie_name = models.CharField(max_length=150)
    release_date = models.IntegerField(
        validators=[
            MaxValueValidator(2100),
            MinValueValidator(1880)
        ],
        default=datetime.datetime.now().year
    )
    movie_poster = models.ImageField(
        upload_to="poster", blank=True)
    movie_description = models.TextField()
    mpaa_rating = models.CharField(max_length=5,
                                   choices=MPAA_RATINGS, default='N/A')
    imdb_rating = models.FloatField(
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ],
    )
    genre_id = models.ManyToManyField(Genre)

    def __str__(self):
        """
        Returns the human readable representation of the object which in this
        case is Movie title. 

        """
        return self.movie_name

    def image_url(self):
        """
        Returns the URL from movie_poster. If an image hasn't been
        uploaded yet, it returns the default image URL.

        """
        if self.movie_poster and hasattr(self.movie_poster, 'url'):
            return self.movie_poster.url
        else:
            return 'images/poster/default.jpg'
