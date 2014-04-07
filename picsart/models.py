# -*- coding: utf-8 -*-

import flickr_api

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class FlickrApi:
    def __init__(self):
        flickr_api.set_keys(api_key=settings.FLICKR_API_KEY, api_secret=settings.FLICKR_SECRET_KEY)
        flickr_api.set_auth_handler(settings.BASE_DIR + '/config/flickr_auth')


class Event(models.Model):
    name = models.CharField(verbose_name='nom', max_length=50)
    organizer = models.CharField(verbose_name='organisateur', max_length=50)
    location = models.CharField(verbose_name='emplacement', default='Compiègne', max_length=50)
    start_date = models.DateField(verbose_name='date de début')
    end_date = models.DateField(verbose_name='date de fin', blank=True, null=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Album(models.Model):
    name = models.CharField(verbose_name='nom', max_length=50)
    event = models.ForeignKey(Event, verbose_name='evenement')
    is_public = models.BooleanField(verbose_name='public', default=False)
    is_published = models.BooleanField(verbose_name='publié', default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)

    def __unicode__(self):
        return self.name


class Photo(models.Model):
    id = models.BigIntegerField(primary_key=True)
    album = models.ForeignKey(Album)
    thumbmail_url = models.URLField()
    medium_url = models.URLField()
    uploader = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    vote = models.PositiveIntegerField(default=0)
    is_public = models.BooleanField(default=False)
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)