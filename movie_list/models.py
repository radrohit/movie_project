from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.
class Movie(models.Model):
	name = models.CharField(max_length = 150)
	release_date = models.DateField()
	poster = models.ImageField(
		default = "")
	description = models.TextField()
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




