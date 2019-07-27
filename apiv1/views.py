from django_filters import rest_framework as filters
from rest_framework import generics

from api.models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    """本モデル用フィルタクラス"""

    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = '__all__'
        # Note:↓のように絞っても、「?price__lte=2000」といった条件は適用される！
        # fields = ('title', 'price',)


class BookListCreateAPIView(generics.ListCreateAPIView):
    """本モデルの取得（一覧）・登録APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = '__all__'
    # Note: あるいは↓のように個別にフィールドを指定する
    # filter_fields = ('title', 'price',)
    # Note: 必要に応じて「filter_fields」の代わりに↓を指定するとさらに柔軟なフィルタリングが可能
    filterset_class = BookFilter


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """本モデルの取得（詳細）・更新・一部更新・削除APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
