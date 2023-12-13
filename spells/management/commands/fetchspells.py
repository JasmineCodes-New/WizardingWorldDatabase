from django.core.management.base import BaseCommand
import requests
from spells.models import Spell


class Command(BaseCommand):
    help = 'Fetches spell data from the Harry Potter API'

    def handle(self, *args, **kwargs):
        response = requests.get('https://hp-api.onrender.com/api/spells')
        if response.status_code == 200:
            spells = response.json()
            for spell_data in spells:
                Spell.objects.update_or_create(
                    name=spell_data['name'],  # Use 'name' field here
                    defaults={
                        'description': spell_data['description']  # And 'description' field here
                    }
                )
            self.stdout.write(self.style.SUCCESS('Successfully updated spells in the database'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch spell data'))

