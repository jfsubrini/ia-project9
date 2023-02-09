"""Web app URL Configuration."""


# Django imports
from django.urls import path

# Import from my app
from . import views



urlpatterns = [
    path('', views.recommender, name='recommender'),
]
