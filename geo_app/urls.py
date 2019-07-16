from django.urls import path, include
from rest_framework import routers

from .views import ContinentView, CountryView, CityView

router = routers.DefaultRouter()
router.register('continents', ContinentView)
router.register('countries', CountryView)
router.register('cities', CityView)

urlpatterns = [
    path('', include(router.urls))
]