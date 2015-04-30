from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Movie(models.Model):
	MPAA_RATINGS = (
		('G', 'General Audience'),
		('PG', 'Parental Guidance'),
		('PG-13', 'Parents Cautioned'),
		('R','Restricted'),
		('NC-17', "Above 17"),
		('N/A',"Not Available"),
		)

	movie_name = models.CharField(max_length = 150)
	release_date = models.DateField()
	movie_poster = models.ImageField(
		default = "")
	movie_description = models.TextField()
	mpaa_rating = models.CharField(max_length =5,
		choices = MPAA_RATINGS, default = 'N/A')
	rating = models.IntegerField(
		validators = [
		MaxValueValidator(10),
		MinValueValidator(0)
		]

		) 
	genre = models.ForeignKey('Genre')

	def __str__(self):
		return self.name


class Genre(models.Model):
	genre_name = models.CharField(max_length = 100)




