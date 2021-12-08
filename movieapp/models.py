
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=50)
    year = models.CharField(max_length=50) 
    genres = models.CharField(max_length=50) 
    summary = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits = 3, decimal_places = 1)
    
class MovieReview(models.Model):
    movie = models.ForeignKey(Movie, models.PROTECT)

    text = models.CharField(max_length=50)
    rating = models.DecimalField(max_digits = 3, decimal_places = 1) 
    created_at = models.DateTimeField(null=True, blank=True)
    summary = models.CharField(max_length=50) 
    is_deleted = models.BooleanField(default=False)

class MovieReviewVote(models.Model):
    review_id = models.ForeignKey(MovieReview, models.PROTECT)

    is_deleted = models.BooleanField(default=False)

