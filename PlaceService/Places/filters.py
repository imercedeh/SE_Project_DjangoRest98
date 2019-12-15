import django_filters
from django_filters import rest_framework as filters
from Places.models import Places
from rest_framework import filters

class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])

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