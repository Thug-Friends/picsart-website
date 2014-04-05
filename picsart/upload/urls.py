from django.conf.urls import patterns, url

from picsart.upload.views import (
    UploadHomeView,
    upload,
    upload_delete,
)

urlpatterns = patterns(
    '',
    url(r'^$',
        UploadHomeView.as_view(),
        name='home'),
    url(r'handle/', upload, name='upload'),
    url(r'^delete/(?P<pk>\d+)$', upload_delete, name='upload_delete'),
)
