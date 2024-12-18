from django.urls import path, include

from posts.views import DashboardView, PostDetailView, PostEditView, PostDeleteView, PostCreateView

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('<int:pk>/', include([
        path('post-detail/', PostDetailView.as_view(), name='post-detail'),
        path('post-edit/', PostEditView.as_view(), name='post-edit'),
        path('post-delete/', PostDeleteView.as_view(), name='post-delete'),
    ])),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
]
