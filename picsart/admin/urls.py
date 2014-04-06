from django.conf.urls import patterns, url

from picsart.admin.views import (
    AdminHome,
    AlbumCreation,
    EventCreation
)

urlpatterns = patterns(
    '',
    url(r'^$',
        AdminHome.as_view(),
        name='home'),
    url(r'album/create', AlbumCreation.as_view(), name='album_create'),
    url(r'event/create', EventCreation.as_view(), name='event_create'),
)
