from rest_framework import serializers

from shop.models import Book


class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        model = Book
        exclude = ['created_at']
