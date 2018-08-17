from django.views.generic import TemplateView
from .models import Tags


class Index(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(Index, self).get_context_data(**kwargs)
        context['page'] = Tags.objects.last()
        return context
