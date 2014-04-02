from django.conf.urls import patterns, url

from picsart.upload.views import (
    UploadHomeView,
)

urlpatterns = patterns(
    '',
    url(r'^$',
        UploadHomeView.as_view(),
        name='home'),
)
