from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.urls import reverse

from .models import Place


def index(request):
    places_geojson = {"type": "FeatureCollection", "features": []}
    places = Place.objects.all()
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.longitude, place.latitude]
            },
            "properties": {
                "title": place.title,
                "placeId": "moscow_legends",
                "detailsUrl": reverse(
                    'place_detail',
                    kwargs={'place_id': place.id})
            }
        }
        places_geojson["features"].append(feature)
    return render(
        request,
        'index.html',
        context={'places_geojson': places_geojson},
    )


def fetch_place(request, place_id):
    place = get_object_or_404(
        Place.objects.prefetch_related('images'),
        pk=place_id,
    )

    place_serialized = {
        "title": place.title,
        "imgs": [image.image.url for image in place.images.all()],
        "description_short": place.description_short,
        "description_long": place.description_long,
        "coordinates": {
            "lng": place.longitude,
            "lat": place.latitude,
        }
    }
    return JsonResponse(
        place_serialized,
        json_dumps_params={'ensure_ascii': False, 'indent': 2},
    )
