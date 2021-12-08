import json
from datetime import datetime

from django.http import HttpResponse
from .models import *

def movieapp_list(request):
    pp = int(request.GET.get('pp',10))
    pg = int(request.GET.get('pg',1))
    title = request.GET.get('title','')
    year = request.GET.get('year','')
    genres = request.GET.get('genres','')
    rating_ordering = request.GET.get('rating_ordering','asc')

    f = models.Q()
    if title: # 검색 조건
        f = f & models.Q(title__icontains=title)
    if year:
        f = f & models.Q(year__icontains=year)
    if genres: 
        f = f & models.Q(genres__icontains=genres)

    movie = Movie.objects.all()
    movie_list = []
    total = 0
    if pg <= 0: pg = 1

    movie = movie.filter(f)
    if rating_ordering == 'asc': # 평점 정렬 조건
        movie = movie.order_by('rating')
    elif rating_ordering == 'desc':
        movie = movie.order_by('-rating')
    else:
        movie = movie.order_by('id')

    for m in movie:
        movie_list.append(m)
        total += 1
    movie_models = movie_list[(pg-1)*pp:pg*pp]

    items=[]
    for m in movie_models :
        v = {}
        v.update({
            'id':m.id, 
            'title':m.title, 
            'year':m.year, 
            'rating':str(m.rating), 
            'genres':m.genres.split(' ')[:len(m.genres.split(' '))-1],
            'summary':m.summary, 
        })
        items.append(v)

    data = {
        'page': pg,
        'total': total,
        'items': items,
    }

    return HttpResponse(json.dumps({'data':data}),
                            content_type='application/json; charset=utf8')

def movieapp_detail(request, movie_id=None):
    try:
        movie = Movie.objects.prefetch_related('moviereview_set').get(id=movie_id)
    except Exception as e: 
        raise Exception("존재하지 않는 영화입니다.",e)

    reviews = []
    for review in movie.moviereview_set.all():
        v = {
            'id': review.id,
            'text': review.text,
            'rating': str(review.rating),
            'created_at': str(review.created_at),
            'summary': review.summary,
        }
        reviews.append(v)

    data = {
        'id': movie.id,
        'title': movie.title,
        'year': movie.year,
        'rating': str(movie.rating),
        'genres': movie.genres.split(' ')[:len(movie.genres.split(' '))-1],
        'summary': movie.summary,
        'reviews': reviews,
    }

    return HttpResponse(json.dumps({'data':data}),
                            content_type='application/json; charset=utf8')

def movieapp_create(request):
    try:
        title = request.POST.get("title")
        year = request.POST.get("year")
        summary = request.POST.get("summary")
        genres = ''
        for genre in request.POST.getlist('genres[]'):
            genres += genre +' '
        movie = Movie(title=title, year=year, genres=genres, summary=summary)
        movie.save()
        succeed = '성공'
    except Exception as e: 
        raise Exception("영화 생성에 실패 하였습니다.",e)

    return HttpResponse(json.dumps({'succeed':succeed}),
                            content_type='application/json; charset=utf8')

def review_detail(request, review_id):
    try:
        review = MovieReview.objects.select_related('movie').get(id=review_id)
    except Exception as e: 
        raise Exception("존재하지 않는 리뷰입니다.",e)

    data = {
        'id': review.id,
        'text': review.text,
        'rating': str(review.rating),
        'created_at': str(review.created_at),
    }

    return HttpResponse(json.dumps({'data':data}),
                            content_type='application/json; charset=utf8')

def review_create(request):
    try:
        movie_id = int(request.POST.get("movie_id"))
        movie = Movie.objects.get(id=movie_id)
        text = request.POST.get("text")
        rating = float(request.POST.get("rating"))
        review = MovieReview(movie=movie, text=text, rating=rating, created_at=datetime.now())
        review.save()
        succeed = '성공'
    except Exception as e: 
        raise Exception("리뷰 생성에 실패 하였습니다.",e)

    return HttpResponse(json.dumps({'succeed':succeed}),
                            content_type='application/json; charset=utf8')

def review_update(request):
    return HttpResponse(json.dumps({'test':"review_update url connect succeed"}),
                            content_type='application/json; charset=utf8')

def review_delete(request):
    return HttpResponse(json.dumps({'test':"review_delete url connect succeed"}),
                            content_type='application/json; charset=utf8')

def vote_create(request):
    return HttpResponse(json.dumps({'test':"vote_create url connect succeed"}),
                            content_type='application/json; charset=utf8')

def vote_delete(request):
    return HttpResponse(json.dumps({'test':"vote_delete url connect succeed"}),
                            content_type='application/json; charset=utf8')



