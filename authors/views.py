from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, UpdateView, DeleteView

from authors.forms import AuthorCreateForm
from authors.models import Author


class AuthorCreateView(View):
    template_name = 'authors/create-author.html'
    form_class = AuthorCreateForm

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            author = form.save(commit=False)
            author.user = request.user
            author.save()
            return redirect('dashboard')
        return render(request, self.template_name, {'form': form})


class AuthorDetailView(DetailView):
    model = Author
    template_name = 'authors/details-author.html'
    context_object_name = 'author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = self.object
        context['posts_count'] = author.posts.count() if hasattr(author, 'posts') else 0
        context['last_post_title'] = author.posts.latest('updated_at').title if context['posts_count'] > 0 else "N/A"
        context['has_author_profile'] = True
        return context


class AuthorEditView(UpdateView):
    model = Author
    template_name = 'authors/edit-author.html'
    fields = ['first_name', 'last_name', 'pets_number', 'info', 'image_url']
    context_object_name = 'author'

    def get_success_url(self):
        return reverse_lazy('detail-author', kwargs={'pk': self.object.pk})


class AuthorDeleteView(DeleteView):
    model = Author
    template_name = 'authors/delete-author.html'
    context_object_name = 'author'
    success_url = reverse_lazy('index')

    def delete(self, request, *args, **kwargs):
        author = self.get_object()
        author.posts.all().delete()
        return super().delete(request, *args, **kwargs)
