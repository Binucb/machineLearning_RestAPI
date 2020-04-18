from django.db import models

# Create your models here.
class PersonDetail(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name

class MovieRating(models.Model):
    movie_name = models.CharField(max_length= 100)
    rating = models.FloatField(max_length=3)

    def __str__(self):
        return self.movie_name +" "+ str(self.rating)