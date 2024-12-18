from django.urls import path

from authors.views import AuthorCreateView, AuthorDetailView, AuthorDeleteView, AuthorEditView

urlpatterns = [
    path('create-author/', AuthorCreateView.as_view(), name='create-author'),
    path('author/<int:pk>/', AuthorDetailView.as_view(), name='detail-author'),
    path('author/delete/<int:pk>/', AuthorDeleteView.as_view(), name='delete-author'),
    path('author/edit/<int:pk>/', AuthorEditView.as_view(), name='edit-author')
]
