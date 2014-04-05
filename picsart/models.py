import flickr_api

from django.conf import settings

class FlickrApi:
    def __init__(self):
        flickr_api.set_keys(api_key = settings.FLICKR_API_KEY, api_secret = settings.FLICKR_SECRET_KEY)
        flickr_api.set_auth_handler(settings.BASE_DIR + '/config/flickr_auth')