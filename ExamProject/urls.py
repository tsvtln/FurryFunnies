from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('authors/', include('authors.urls')),
    path('dashboard/', include('posts.urls')),
]
