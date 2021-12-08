from django.contrib import admin
from .models import Movie, MovieReview, MovieReviewVote

class MovieAdmin(admin.ModelAdmin) :
    list_display = ('title', 'year', 'genres', 'summary', 'rating' )

class MovieRevieweAdmin(admin.ModelAdmin) :
    list_display = ('movie', 'text', 'rating', 'created_at', 'is_deleted' )

class MovieReviewVoteeAdmin(admin.ModelAdmin) :
    list_display = ('review_id', 'is_deleted')

admin.site.register(Movie, MovieAdmin) 
admin.site.register(MovieReview, MovieRevieweAdmin)
admin.site.register(MovieReviewVote, MovieReviewVoteeAdmin)