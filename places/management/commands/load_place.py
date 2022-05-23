import requests

from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile

from places.models import Place, Image


class Command(BaseCommand):
    help = 'To load place specify link with json-formatted info about'

    def add_arguments(self, parser):
        parser.add_argument('place_json', nargs='+', type=str)

    def handle(self, *args, **options):
        for link in options['place_json']:
            response = requests.get(link)
            response.raise_for_status()
            place_serialized = response.json()
            place, created = Place.objects.get_or_create(
                title=place_serialized['title'],
                defaults={
                    'description_short': place_serialized['description_short'],
                    'description_long': place_serialized['description_long'],
                    'latitude': place_serialized['coordinates']['lat'],
                    'longitude': place_serialized['coordinates']['lng'],
                }
            )
            if created:
                for index, image_link in enumerate(place_serialized['imgs'], start=1):
                    response = requests.get(image_link)
                    response.raise_for_status()
                    image_binary = ContentFile(response.content)
                    image = Image(place=place)
                    image.image.save(
                        f'{place.title}_{index}.jpg',
                        image_binary,
                        save=True
                    )
                    image.save()
            self.stdout.write(self.style.SUCCESS('Successfully added new place'))
