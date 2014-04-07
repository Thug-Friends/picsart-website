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
    url(r'^backoffice/', include('picsart.backoffice.urls', namespace='backoffice')),
    url(r'^login/$', 'django_cas.views.login',  name='auth_login'),
    url(r'^logout/$', 'django_cas.views.logout',  name='auth_logout')
)
