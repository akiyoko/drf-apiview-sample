from rest_framework import generics
from rest_framework.response import Response

from api.models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):
    """本モデルの取得（一覧）・登録APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """本モデルの取得（詳細）・更新・一部更新・削除APIクラス"""

    queryset = Book.objects.all()
    serializer_class = BookSerializer
