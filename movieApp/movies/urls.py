from django.urls import path
from .import views


urlpatterns = [
    path("", views.index, name="homePage"),
    path("movies", views.movies, name="moviesPage"),
    path("movies/<slug:slug>", views.movieDetails, name="movieDetails")
]
