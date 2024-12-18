from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from authors.models import Author
from posts.forms import PostEditForm, PostCreateForm
from posts.models import Posts


class DashboardView(ListView):
    model = Posts
    template_name = 'dashboard.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Posts.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        author = Author.objects.first()
        context['has_author_profile'] = bool(author)
        context['author'] = author

        return context


class PostCreateView(CreateView):
    model = Posts
    form_class = PostCreateForm
    template_name = 'posts/create-post.html'
    success_url = reverse_lazy('dashboard')


class PostDetailView(DetailView):
    model = Posts
    template_name = 'posts/details-post.html'
    context_object_name = 'post'


class PostEditView(UpdateView):
    model = Posts
    form_class = PostEditForm
    template_name = 'posts/edit-post.html'

    def get_success_url(self):
        return reverse_lazy('post-detail', kwargs={
            'pk': self.object.pk
        })


class PostDeleteView(DeleteView):
    model = Posts
    template_name = 'posts/delete-post.html'
    success_url = reverse_lazy('dashboard')
