from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin1234/', admin.site.urls),
    path('', include('posts.urls')),
]
