from django.forms import ModelForm

from picsart.models import Album, Event


class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ['event', 'name', 'is_public']


class EventForm(ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'organizer', 'location', 'start_date', 'end_date']