from django.core.management.base import BaseCommand
import requests
from characters.models import Character, Wand


class Command(BaseCommand):
    help = 'Fetches data from the Harry Potter API and populates the database'

    def handle(self, *args, **options):
        self.stdout.write("Fetching data from the Harry Potter API...")
        response = requests.get("https://hp-api.onrender.com/api/characters")
        if response.status_code == 200:
            characters = response.json()
            for char_data in characters:
                character, created = Character.objects.update_or_create(
                    character_id=char_data['id'],
                    defaults={
                        'name': char_data['name'],
                        'species': char_data['species'],
                        'gender': char_data['gender'],
                        'house': char_data['house'],
                        'date_of_birth': char_data['dateOfBirth'],
                        'year_of_birth': char_data['yearOfBirth'],
                        'wizard': char_data['wizard'],
                        'ancestry': char_data['ancestry'],
                        'eye_color': char_data['eyeColour'],
                        'hair_color': char_data['hairColour'],
                        'patronus': char_data['patronus'],
                        'hogwarts_student': char_data['hogwartsStudent'],
                        'hogwarts_staff': char_data['hogwartsStaff'],
                        'actor': char_data['actor'],
                        'alive': char_data['alive'],
                        'image_url': char_data['image']
                    }
                )

                # Check if wand data is present and complete
                wand_data = char_data.get('wand')
                if wand_data and all(wand_data.get(field) is not None for field in ['wood', 'core', 'length']):
                    Wand.objects.update_or_create(
                        character=character,
                        defaults={
                            'wood': wand_data['wood'],
                            'core': wand_data['core'],
                            'length': wand_data['length']
                        }
                    )
            self.stdout.write(self.style.SUCCESS('Successfully updated database'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch data from API'))


