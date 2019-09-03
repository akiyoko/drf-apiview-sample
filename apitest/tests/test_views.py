from django.utils import timezone
from rest_framework.test import APITestCase

from apitest.models import Book


class TestBookListCreateAPIView(APITestCase):
    """TODO: テストクラス"""

    TARGET_URL = '/api/test/books/'
    TARGET_URL_WITH_PK = '/api/test/books/{pk}/'

    def test_create_success(self):
        """TODO: テストメソッド"""

        # APIリクエストを実行
        params = {
            'title': 'aaa',
            'price': 1000,
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # データベースの状態を検証
        self.assertEqual(Book.objects.count(), 1)
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 201)
        book = Book.objects.get()
        expected_data = {
            'id': str(book.id),
            'title': book.title,
            'price': book.price,
            'created_at': str(timezone.localtime(book.created_at)).replace(' ', 'T'),
        }
        self.assertJSONEqual(response.content, expected_data)

    def test_create_invalid(self):
        """TODO: テストメソッド"""

        # APIリクエストを実行
        params = {
            'title': '',
            'price': 1000,
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # データベースの状態を検証
        self.assertEqual(Book.objects.count(), 0)
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 400)
        self.assertCountEqual([x for x in response.data], ['title'])
        self.assertCountEqual([x.code for x in response.data['title']], ['blank'])

# class TestBookListCreateAPIView2(APITestCase):
#     TARGET_URL = '/api/v1/books/'
#     TARGET_URL_WITH_PK = '/api/v1/books/{pk}/'
#
#     # TODO
#     def test_list_success(self):
#         book = Book.objects.create(title='test', price=1000)
#         input_params = {
#             'title': book.title,
#             'price': book.price,
#         }
#         # レスポンス取得
#         response = self.client.get(self.TARGET_URL)
#
#         # 結果判定
#         self.assertEqual(response.status_code, 200)
#         expected_data = [{
#             'id': str(book.id),
#             'title': book.title,
#             'price': book.price,
#         }]
#         content_data = json.loads(response.content.decode('utf-8'))
#         self.assertEqual(len(content_data), 1)
#         for expected, actual in zip(expected_data, content_data):
#             self.assertDictEqual(actual, expected)
#
#     # TODO
#     def test_create_success(self):
#         params = {
#             'title': 'test',
#             'price': 1000,
#         }
#         # レスポンス取得
#         response = self.client.post(self.TARGET_URL, params, format='json')
#
#         # 結果判定
#         self.assertEqual(response.status_code, 201)
#         book = Book.objects.get(title=params['title'])
#         expected_data = {
#             'id': str(book.id),
#             **params,
#         }
#         content_data = json.loads(response.content.decode('utf-8'))
#         self.assertEqual(content_data, expected_data)
