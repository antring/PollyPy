from django.conf.urls import url
from .views import tvupload, movieupload, upload_index


urlpatterns = [
    url(r'^$', view=upload_index, name='index'),
    url(r'tv', view=tvupload, name='tv'),
    url(r'movie', view=movieupload, name='movie')
]
