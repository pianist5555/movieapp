from django.urls import path
from movieapp import views

urlpatterns_movie = [
    path('list', views.movieapp_list, name='api_movie_list'),
    path('detail/<int:movie_id>', views.movieapp_detail, name='api_movie_detail'),
    path('create', views.movieapp_create, name='api_movie_create'),
]
urlpatterns_review = [
    path('detail/<int:review_id>', views.review_detail, name='api_review_detail'),
    path('create', views.review_create, name='api_review_create'),
    path('update', views.review_update, name='api_review_update'),
    path('delete', views.review_delete, name='api_review_delete'),
]
urlpatterns_vote = [
    path('list', views.vote_create, name='api_vote_create'),
    path('detail', views.vote_delete, name='api_vote_delete'),
]