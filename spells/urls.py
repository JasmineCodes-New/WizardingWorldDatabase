from django.urls import path
from . import views

urlpatterns = [
    path('spells/', views.spell_list, name='spell_list'),
]
