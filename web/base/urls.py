# Django
from django.urls import path
# Project
from base import views as baseViews

urlpatterns = [
    path('', baseViews.landing, name='landing'),
]