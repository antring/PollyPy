from django.shortcuts import render
from .forms import TvForm, MovieForm
from .models import TvSub, MovieSub


def tvupload(request):
    tvform = TvForm(request.POST or None)

    if request.POST:
        tvform.save()
        returnstring = 'TVsub upload complete'

        tvsubs = TvSub.objects.filter(name__contains='as')

        return render(request, 'upload_complete_template.html', {'msg': returnstring, 'subs': tvsubs})

    return render(request, 'upload_template.html', {'tvform': tvform})


