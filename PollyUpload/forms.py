from django.forms import ModelForm
from .models import TvSub, MovieSub


class TvForm(ModelForm):

    class Meta:
        model = TvSub
        fields = ['name', 'season', 'episode', 'lang']


class MovieForm(ModelForm):

    class Meta:
        model = MovieSub
        fields = ['name', 'year', 'lang']
