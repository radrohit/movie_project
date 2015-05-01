from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
import datetime
import os
# Create your models here.
class Genre(models.Model):
	genre_name = models.CharField(max_length = 100)
	genre_description = models.TextField(max_length = 300,default = "")
	
	def __unicode__(self):
		return self.genre_name

	def __str__(self):
		return self.genre_name


class Movie(models.Model):
	MPAA_RATINGS = (
		('G', 'G'),
		('PG', 'PG'),
		('PG-13', 'PG-13'),
		('R','R'),
		('NC-17', "NC-17"),
		('N/A',"Not Available"),
		)
	movie_name = models.CharField(max_length = 150)
	release_date = models.IntegerField( 
		validators = [
		MaxValueValidator(2100),
		MinValueValidator(1880)],
		default = datetime.datetime.now().year)
	movie_poster = models.ImageField(
		upload_to = "poster", blank = True)
	movie_description = models.TextField()
	mpaa_rating = models.CharField(max_length =5,
		choices = MPAA_RATINGS, default = 'N/A')
	rating = models.FloatField(
		validators = [
		MaxValueValidator(10),
		MinValueValidator(0)
		],

		) 
	genre_id = models.ManyToManyField(Genre)

	def __str__(self):
		return self.movie_name

	def image_url(self):
		"""
		Returns the URL of the image associated with this Object.
		If an image hasn't been uploaded yet, it returns a stock image

		:returns: str -- the image url
		"""
		if self.movie_poster and hasattr(self.movie_poster, 'url'):
			return self.movie_poster.url
		else:
			return 'images/poster/default.jpg'





