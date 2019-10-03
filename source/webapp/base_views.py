from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404


class DetailView(TemplateView):
    context_key = 'objects'
    model = None
    pk_url = 'pk'

    def get_context_data(self, **kwargs):
        pk = kwargs.get(self.pk_url)
        context = super().get_context_data(**kwargs)
        context[self.context_key] = get_object_or_404(self.model, pk=pk)
        return context
