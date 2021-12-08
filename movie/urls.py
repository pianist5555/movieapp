
from django.contrib import admin
from django.urls import path,include

from movieapp import urls as movieapp_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movie/', include(movieapp_urls.urlpatterns_movie)),
    path('review/', include(movieapp_urls.urlpatterns_review)),
    path('vote/', include(movieapp_urls.urlpatterns_vote)),
]
