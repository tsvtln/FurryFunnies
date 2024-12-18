from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView
from django.views.generic.edit import BaseFormView

from authors.models import Author


class IndexView(TemplateView):
    template_name = 'index.html'
    success_url = reverse_lazy('index.html')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.first()
        if author:
            context['has_author_profile'] = True
            context['author'] = author
        else:
            context['has_author_profile'] = False

        return context
