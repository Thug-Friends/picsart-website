from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = 'home/homepage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(
            HomePageView,
            self,
        ).get_context_data(*args, **kwargs)
        return context
