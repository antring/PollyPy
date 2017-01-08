from django.conf.urls import url
from .views import tvupload, movieupload

urlpatterns = [
    url(r'tv', view=tvupload),
    url(r'movie', view=movieupload)
]
