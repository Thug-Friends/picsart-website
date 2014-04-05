import os
import flickr_api

from django.core.urlresolvers import reverse
from django.views.generic import TemplateView
from django.views.decorators.http import require_POST
from jfu.http import upload_receive, UploadResponse, JFUResponse
from picsart.models import FlickrApi

api = FlickrApi()

class UploadHomeView(TemplateView):
    template_name = 'upload/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            UploadHomeView,
            self,
        ).get_context_data(*args, **kwargs)
        context['accepted_mime_types'] = ['image/*']
        return context


@require_POST
def upload(request):
    file = upload_receive(request)

    tmp_file = open(file.name, 'wb+')

    for chunk in file.chunks():
        tmp_file.write(chunk)

    tmp_file.close()
    photo = flickr_api.upload(photo_file=tmp_file.name, title=tmp_file.name, is_public=0)

    basename = os.path.basename(tmp_file.name)

    sizes = photo.getSizes()

    file_dict = {
        'name': basename,
        'size': file.size,
        'url': sizes['Original']['source'],
        'thumbnailUrl': sizes['Thumbnail']['source'],
        'deleteUrl': reverse('upload:upload_delete', kwargs={'pk': photo.id}),
        'deleteType': 'POST',
    }

    os.unlink(tmp_file.name)

    return UploadResponse(request, file_dict)


@require_POST
def upload_delete(request, pk):
    success = True
    try:
        photo = flickr_api.Photo(id=pk)
        photo.delete()
    except flickr_api.FlickrAPIError:
        success = False
    return JFUResponse(request, success)