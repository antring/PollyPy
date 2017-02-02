from django.conf.urls import url
from .views import management_index

urlpatterns = [
    url(r'^$', view=management_index, name='index'),
]
