# views.py
# characters/views.py

from django.shortcuts import render
from .models import Character


def characters_list(request):
    characters = Character.objects.all()
    return render(request, 'characters_list.html', {'characters': characters})


