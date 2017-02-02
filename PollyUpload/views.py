from django.shortcuts import render
from .forms import TvForm, MovieForm
from .models import TvSub, MovieSub


def upload_index(request):
    return render(request, 'start_template.html', {})


def tvupload(request):
    tvform = TvForm(request.POST or None)

    if request.POST:
        tvform.save()
        returnstring = 'TVsub upload complete'
        # tvsubs = TvSub.objects.all()

        return render(request, 'upload_complete_template.html', {'msg': returnstring, 'test': tvform_name})

    return render(request, 'upload_template.html', {'form': tvform, 'formtype': 'TV'})


def movieupload(request):
    movieform = MovieForm(request.POST or None)

    if request.POST:
        movieform.save()
        returnstring = 'MovieSub upload complete'

        return render(request, 'upload_complete_template.html', {'msg': returnstring})

    return render(request, 'upload_template.html', {'form': movieform, 'formtype': 'Film'})
