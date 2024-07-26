import django_filters
from .models import Task

class TaskFilter(django_filters.FilterSet):
    created_by=django_filters.NumberFilter(field_name='created_by',lookup_expr='exact')
    assigned_to=django_filters.NumberFilter(field_name=' assigned_to',lookup_expr='exact')
    created_on_start = django_filters.DateFilter(field_name='created_on',lookup_expr='gte')
    created_on_end = django_filters.DateFilter(field_name='created_on',lookup_expr='lte')
    status=django_filters.CharFilter(field_name='status',lookup_expr='exact')

    class Meta:
        model= Task
        fields='__all__'