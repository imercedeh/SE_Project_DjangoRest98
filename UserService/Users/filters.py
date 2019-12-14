import django_filters
from django_filters import rest_framework as filters
from Places.models import Places
from rest_framework import filters

class CustomSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
        # #self.request.query_params.get('search')
        # if request.query_params.get('id', 'user'):
        #     return ['id', 'user']
        # return super(CustomSearchFilter, self).get_search_fields(view, request)
