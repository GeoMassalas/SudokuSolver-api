from django_filters import rest_framework as filters
from core.models import SudokuModel


class SudokuFilter(filters.FilterSet):
    min_clues = filters.NumberFilter(field_name="clues", lookup_expr='gte')
    max_clues = filters.NumberFilter(field_name="clues", lookup_expr='lte')
    min_difficulty = filters.NumberFilter(field_name="difficulty", lookup_expr='gte')
    max_difficulty = filters.NumberFilter(field_name="difficulty", lookup_expr='lte')

    class Meta:
        model = SudokuModel
        fields = ['difficulty', 'dataset_id', 'dataset', 'min_clues', 'max_clues', 'min_difficulty', 'max_difficulty']
