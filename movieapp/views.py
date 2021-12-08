import json

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
    if rating_ordering == 'asc': # 평점 역순 여부
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

def movieapp_detail(request):
    return HttpResponse(json.dumps({'test':"movieapp_detail url connect succeed"}),
                            content_type='application/json; charset=utf8')

def movieapp_create(request):
    return HttpResponse(json.dumps({'test':"movieapp_create url connect succeed"}),
                            content_type='application/json; charset=utf8')

def review_detail(request):
    return HttpResponse(json.dumps({'test':"review_detail url connect succeed"}),
                            content_type='application/json; charset=utf8')

def review_create(request):
    return HttpResponse(json.dumps({'test':"review_create url connect succeed"}),
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



