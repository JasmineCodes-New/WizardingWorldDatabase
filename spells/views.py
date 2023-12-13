from django.shortcuts import render
from .models import Spell


def spell_list(request):
    spells = Spell.objects.all()
    return render(request, 'spell_list.html', {'spells': spells})