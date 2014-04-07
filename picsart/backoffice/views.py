from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse_lazy
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import HttpResponse
from django.utils import simplejson
from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView, UpdateView

from braces.views import LoginRequiredMixin, GroupRequiredMixin

from picsart.models import Album, Event


class AdminHome(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'backoffice/homepage.html'
    raise_exception = True
    group_required = 'bureau'

    def get_context_data(self, *args, **kwargs):
        context = super(
            AdminHome,
            self,
        ).get_context_data(*args, **kwargs)
        return context


class AlbumCreation(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    template_name = 'backoffice/album/album_creation_form.html'
    raise_exception = True
    group_required = 'bureau'
    model = Album
    fields = ['event', 'name', 'is_public']
    success_url = reverse_lazy('backoffice:album_view')

    def form_valid(self, form):
        album = form.save(commit=False)
        album.created_by = self.request.user
        album.save()
        return super(AlbumCreation, self).form_valid(form)


class EventCreation(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    template_name = 'backoffice/event/event_creation_form.html'
    raise_exception = True
    group_required = 'bureau'
    model = Event
    fields = ['name', 'organizer', 'location', 'start_date', 'end_date']
    success_url = reverse_lazy('backoffice:event_view')

    def form_valid(self, form):
        event = form.save(commit=False)
        event.created_by = self.request.user
        event.save()
        return super(EventCreation, self).form_valid(form)


class AlbumPaginationView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'backoffice/album/album_pagination.html'
    raise_exception = True
    group_required = 'bureau'

    def get_context_data(self, **kwargs):
        context = super(AlbumPaginationView, self).get_context_data(**kwargs)
        events = Album.objects.all().order_by('-created_at')
        paginator = Paginator(events, 10)
        page = self.request.GET.get('page')
        try:
            show_events = paginator.page(page)
        except PageNotAnInteger:
            show_events = paginator.page(1)
        except EmptyPage:
            show_events = paginator.page(paginator.num_pages)
        context['albums'] = show_events
        return context


class EventPaginationView(LoginRequiredMixin, GroupRequiredMixin, TemplateView):
    template_name = 'backoffice/event/event_pagination.html'
    raise_exception = True
    group_required = 'bureau'

    def get_context_data(self, **kwargs):
        context = super(EventPaginationView, self).get_context_data(**kwargs)
        events = Event.objects.all().order_by('-created_at')
        paginator = Paginator(events, 10)
        page = self.request.GET.get('page')
        try:
            show_events = paginator.page(page)
        except PageNotAnInteger:
            show_events = paginator.page(1)
        except EmptyPage:
            show_events = paginator.page(paginator.num_pages)
        context['events'] = show_events
        return context


class AlbumDelete(LoginRequiredMixin, GroupRequiredMixin, View):
    raise_exception = True
    group_required = 'bureau'

    def post(self, request, **kwargs):
        pk_album = request.POST['album_id']
        try:
            album = Album.objects.get(pk=pk_album)
            album.delete()
        except ObjectDoesNotExist:
            pass
        result = {'success': True, "album_id": pk_album}
        return HttpResponse(simplejson.dumps(result))


class EventDelete(LoginRequiredMixin, GroupRequiredMixin, View):
    raise_exception = True
    group_required = 'bureau'

    def post(self, request, **kwargs):
        pk_event = request.POST['event_id']
        try:
            event = Event.objects.get(pk=pk_event)
            event.delete()
        except ObjectDoesNotExist:
            pass
        result = {'success': True, "event_id": pk_event}
        return HttpResponse(simplejson.dumps(result))


class EventEdition(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    template_name = 'backoffice/event/event_edition_form.html'
    raise_exception = True
    group_required = 'bureau'
    model = Event
    fields = ['name', 'organizer', 'location', 'start_date', 'end_date']
    success_url = reverse_lazy('backoffice:event_view')


class AlbumEdition(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    template_name = 'backoffice/album/album_edition_form.html'
    raise_exception = True
    group_required = 'bureau'
    model = Album
    fields = ['name', 'event', 'is_public', 'is_published']
    success_url = reverse_lazy('backoffice:album_view')
