from django.shortcuts import render
from PollyUpload.models import MovieSub, TvSub


def management_index(request):
    return render(request, 'management_index.html', {})


def render_data(request):
    return
