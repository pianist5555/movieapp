import json

from django.http import HttpResponse

def movieapp_list(request):
    return HttpResponse(json.dumps({'test':"movieapp_list url connect succeed"}),
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



