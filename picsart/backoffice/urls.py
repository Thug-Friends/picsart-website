from django.conf.urls import patterns, url

from picsart.backoffice.views import (
    AdminHome,
    AlbumCreation,
    AlbumEdition,
    AlbumPaginationView,
    AlbumDelete,
    EventCreation,
    EventPaginationView,
    EventDelete,
    EventEdition
)

urlpatterns = patterns(
    '',
    url(r'^$',
        AdminHome.as_view(),
        name='home'),
    url(r'album/create/$', AlbumCreation.as_view(), name='album_create'),
    url(r'album/edit/(?P<pk>\d+)$', AlbumEdition.as_view(), name='album_edit'),
    url(r'album/view/$', AlbumPaginationView.as_view(), name='album_view'),
    url(r'album/delete/$', AlbumDelete.as_view(), name='album_delete'),
    url(r'event/create/$', EventCreation.as_view(), name='event_create'),
    url(r'event/edit/(?P<pk>\d+)$', EventEdition.as_view(), name='event_edit'),
    url(r'event/view/$', EventPaginationView.as_view(), name='event_view'),
    url(r'event/delete/$', EventDelete.as_view(), name='event_delete'),
)
