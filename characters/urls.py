# characters/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('characters/', views.characters_list, name='characters_list'),
]
