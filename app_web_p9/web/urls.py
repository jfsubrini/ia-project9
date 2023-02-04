"""Web app URL Configuration."""


# Django imports
from django.urls import path

# Import from my app
from . import views



urlpatterns = [
    path('recommender-get/<int:pk>/', views.Recommender.as_view(), name='recommender'),
]
