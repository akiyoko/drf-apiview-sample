from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import status, views
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

from .models import Book
from .serializers import BookSerializer


class BookFilter(filters.FilterSet):
    """本モデル用フィルタクラス"""

    price__lte = filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Book
        fields = '__all__'


class BookListCreateAPIView(views.APIView):
    """本モデルの取得（一覧）・登録APIクラス"""

    def get(self, request, *args, **kwargs):
        """本モデルの取得（一覧）APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        queryset = Book.objects.all()
        # フィルタリング
        filterset = BookFilter(request.query_params, queryset=queryset)
        if not filterset.is_valid():
            # クエリ文字列のバリデーションがNGの場合は400エラー
            # Note: DateFilterは「YYYY-MM-DD」、DateTimeFilterは「YYYY-MM-DD hh:mm:ss」で指定
            raise ValidationError(filterset.errors)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=filterset.qs, many=True)
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """本モデルの登録APIに対応するハンドラメソッド"""

        # シリアライザオブジェクトを作成
        serializer = BookSerializer(data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを登録
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_201_CREATED)


class BookRetrieveUpdateDestroyAPIView(views.APIView):
    """本モデルの取得（詳細）・更新・一部更新・削除APIクラス"""

    def get(self, request, pk, *args, **kwargs):
        """本モデルの取得（詳細）APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk, *args, **kwargs):
        """本モデルの更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def patch(self, request, pk, *args, **kwargs):
        """本モデルの一部更新APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # シリアライザオブジェクトを作成
        serializer = BookSerializer(instance=book, data=request.data, partial=True)
        # バリデーションを実行
        serializer.is_valid(raise_exception=True)
        # モデルオブジェクトを一部更新
        serializer.save()
        # レスポンスオブジェクトを作成して返す
        return Response(serializer.data, status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        """本モデルの削除APIに対応するハンドラメソッド"""

        # モデルオブジェクトを取得
        book = get_object_or_404(Book, pk=pk)
        # モデルオブジェクトを削除
        book.delete()
        # レスポンスオブジェクトを作成して返す
        return Response(status=status.HTTP_204_NO_CONTENT)
