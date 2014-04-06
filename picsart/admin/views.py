from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import TemplateView

from picsart.admin.forms import AlbumForm, EventForm

class AdminHome(TemplateView):
    template_name = 'admin/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            AdminHome,
            self,
        ).get_context_data(*args, **kwargs)
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AdminHome, self).dispatch(request, *args, **kwargs)


class AlbumCreation(TemplateView):
    template_name = 'admin/album_creation_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            AlbumCreation,
            self,
        ).get_context_data(*args, **kwargs)
        context['form'] = AlbumForm()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(AlbumCreation, self).dispatch(request, *args, **kwargs)


class EventCreation(TemplateView):
    template_name = 'admin/event_creation_form.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            EventCreation,
            self,
        ).get_context_data(*args, **kwargs)
        context['form'] = EventForm()
        return context

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(EventCreation, self).dispatch(request, *args, **kwargs)
