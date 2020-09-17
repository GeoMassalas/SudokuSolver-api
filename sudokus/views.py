from rest_framework.viewsets import ModelViewSet
from django_filters import rest_framework as filters
from core.filters import SudokuFilter
from core.models import SudokuModel
from core.permissions import IsAdminOrReadOnly
from sudokus.serializers import SudokuSerializer


class SudokuViewSet(ModelViewSet):
    queryset = SudokuModel.objects.all()
    serializer_class = SudokuSerializer
    permission_classes = [IsAdminOrReadOnly, ]
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = SudokuFilter
