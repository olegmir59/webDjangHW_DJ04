from django.urls import path
from . import views

app_name = 'films'  # Важно для namespace

urlpatterns = [
    path('add/', views.add_movie, name='add_movie'),
    path('list/', views.movie_list, name='movie_list'),
]