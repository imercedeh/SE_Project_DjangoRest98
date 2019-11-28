import django_filters
from django_filters import rest_framework as filters

from Places.models import Places


class PlacesFilter(django_filters.FilterSet):
    class Meta:
        model = Places
        fields = [
        'id',
        'title', 
        'Likes',
        'categories',
        'Hardness',
        'Time',
        'StartTime',
        'EndTime',
        'City',
        ]