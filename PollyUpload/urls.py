from django.conf.urls import url, include
from .views import tvupload

urlpatterns = [
    url(r'^', view=tvupload)
]