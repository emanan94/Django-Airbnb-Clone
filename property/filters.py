import django_filters
from .models import Property

class PropertyFilter(django_filters.FilterSet):
    price= django_filters.NumberFilter( lookup_expr='lt')
    title=django_filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Property
        fields = ['title','place', 'category']