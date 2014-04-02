from django.conf.urls import patterns, url, include

from picsart.views import (
    HomePageView,
)

urlpatterns = patterns(
    '',
    url(r'^$',
        HomePageView.as_view(),
        name='home'),
    url(r'^upload/', include('picsart.upload.urls', namespace='upload')),
)
