from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('films/', include('films.urls')),
    path('', lambda request: redirect('films:add_movie')),  # Корневая страница
]
