from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views


urlpatterns = [
    path('', views.index),
    path('places/<int:place_id>/', views.fetch_place, name='place_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
