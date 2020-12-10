from django_filters import rest_framework as filters
from rest_framework import viewsets

from shop.models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    """本モデル用フィルタクラス"""

    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = '__all__'


class BookViewSet(viewsets.ModelViewSet):
    """本モデルのCRUD用APIクラス"""

    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = BookFilter
