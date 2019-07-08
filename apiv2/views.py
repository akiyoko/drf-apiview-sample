from django_filters import rest_framework as filters
from rest_framework import viewsets

from api.models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = '__all__'


class BookViewSet(viewsets.ModelViewSet):
    """本のCRUD用API"""
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = BookFilter
