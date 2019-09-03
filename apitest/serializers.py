from rest_framework import serializers

from .models import Book


class BookSerializer(serializers.ModelSerializer):
    """本モデル用シリアライザ"""

    class Meta:
        model = Book
        fields = '__all__'
