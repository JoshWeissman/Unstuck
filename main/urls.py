from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("review", views.review, name="review"),
    path("reviews", views.reviews, name="reviews")
]
