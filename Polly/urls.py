from django.conf.urls import url, include
from .views import index


urlpatterns = [
    url(r'^$', view=index),
    url(r'^upload', include('PollyUpload.urls')),
]
