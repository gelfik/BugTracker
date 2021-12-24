from django_filters import rest_framework as filters

from .models import SubSystemModel


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class SubSystemFilter(filters.FilterSet):
    product = CharFilterInFilter(field_name='product__title', lookup_expr='in')
    status_type = CharFilterInFilter(field_name='status_type', lookup_expr='in')

    class Meta:
        model = SubSystemModel
        fields = ['product']
