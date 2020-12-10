from django.test import TestCase
from django.utils.timezone import localtime

from apitest.serializers import BookSerializer
from shop.models import Book


class TestBookSerializer(TestCase):
    """BookSerializerのテストクラス"""

    def test_input_valid(self):
        """入力データのバリデーション（OK）"""

        # シリアライザを作成
        input_data = {
            'title': 'aaa',
            'price': 111,
        }
        serializer = BookSerializer(data=input_data)

        # バリデーションの結果を検証
        self.assertEqual(serializer.is_valid(), True)

    def test_input_invalid_if_title_is_blank(self):
        """入力データのバリデーション（NG：titleが空文字）"""

        # シリアライザを作成
        input_data = {
            'title': '',
            'price': 111,
        }
        serializer = BookSerializer(data=input_data)

        # バリデーションの結果を検証
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ['title'])
        self.assertCountEqual(
            [x.code for x in serializer.errors['title']],
            ['blank'],
        )

    def test_input_invalid_if_title_is_blank_and_price_is_invalid(self):
        """入力データのバリデーション（NG：titleが空文字、priceが数値でない）"""

        # シリアライザを作成
        input_data = {
            'title': '',
            'price': 'bbb',
        }
        serializer = BookSerializer(data=input_data)

        # バリデーションの結果を検証
        self.assertEqual(serializer.is_valid(), False)
        self.assertCountEqual(serializer.errors.keys(), ['title', 'price'])
        self.assertCountEqual(
            [x.code for x in serializer.errors['title']],
            ['blank'],
        )
        self.assertCountEqual(
            [x.code for x in serializer.errors['price']],
            ['invalid'],
        )

    def test_output_data(self):
        """出力データの内容検証"""

        # シリアライザを作成
        book = Book.objects.create(
            title='aaa',
            price=111,
        )
        serializer = BookSerializer(instance=book)

        # シリアライザの出力内容を検証
        expected_data = {
            'id': str(book.id),
            'title': book.title,
            'price': book.price,
            'publisher': None,
            'authors': [],
            'created_at': str(localtime(book.created_at)).replace(' ', 'T'),
        }
        self.assertDictEqual(serializer.data, expected_data)
