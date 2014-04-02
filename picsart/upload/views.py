from django.views.generic import TemplateView


class UploadHomeView(TemplateView):
    template_name = 'upload/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            UploadHomeView,
            self,
        ).get_context_data(*args, **kwargs)
        return context
