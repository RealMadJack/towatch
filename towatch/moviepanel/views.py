from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView, ListView, TemplateView

from .models import MoviePanel


class MoviePanelView(ListView):
    """Movie panel view"""

    template_name = 'moviepanel/index.html'

    def get(self, request, *args, **kwargs):
        try:
            if kwargs:
                moviepanel = MoviePanel.objects.get(slug=kwargs['moviepanel_slug'])
            else:
                moviepanel = MoviePanel.objects.first()

            context = {'moviepanel': moviepanel}

            return render(
                request,
                context=context,
                template_name=self.template_name)
        except MoviePanel.DoesNotExist:
            return redirect('/404/')
