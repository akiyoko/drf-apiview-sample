from django.utils import timezone
from rest_framework.test import APITestCase

from apitest.models import Book
from apitest.serializers import BookSerializer


class TestBookSerializer(APITestCase):

    def test_for_retrieve(self):
        # シリアライザを作成
        book = Book.objects.create(title='test', price=1000)
        serializer = BookSerializer(instance=book)

        # 検証
        expected_data = {
            'id': str(book.id),
            'title': book.title,
            'price': book.price,
            'created_at': str(timezone.localtime(book.created_at)).replace(' ', 'T'),
            # ↓extra_kwargsを使ってcreated_atのオプションをformat='%Y-%m-%dT%H:%M:%S.%f'とした場合
            # 'created_at': timezone.localtime(book.created_at).strftime('%Y-%m-%dT%H:%M:%S.%f'),
        }
        self.assertDictEqual(serializer.data, expected_data)
