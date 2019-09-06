from django.contrib.auth import get_user_model
from django.utils.timezone import localtime
from rest_framework.test import APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from apitest.models import Book


class TestBookCreateAPIView(APITestCase):
    """BookCreateAPIViewのテストクラス"""

    TARGET_URL = '/api/test/books/'

    def test_create_success(self):
        """本モデルの登録APIへのPOSTリクエスト（正常系）"""

        # APIリクエストを実行
        params = {
            'title': 'aaa',
            'price': 111,
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # データベースの状態を検証
        self.assertEqual(Book.objects.count(), 1)
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 201)
        book = Book.objects.get()
        expected_json_dict = {
            'id': str(book.id),
            'title': book.title,
            'price': book.price,
            'created_at': str(localtime(book.created_at)).replace(' ', 'T'),
        }
        self.assertJSONEqual(response.content, expected_json_dict)

    def test_create_bad_request(self):
        """本モデルの登録APIへのPOSTリクエスト（異常系：バリデーションNG）"""

        # APIリクエストを実行
        params = {
            'title': '',
            'price': 111,
        }
        response = self.client.post(self.TARGET_URL, params, format='json')

        # データベースの状態を検証
        self.assertEqual(Book.objects.count(), 0)
        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 400)


class TestBookUpdateAPIView(APITestCase):
    """BookUpdateAPIViewのテストクラス"""

    TARGET_URL_WITH_PK = '/api/test/books/{}/'

    @classmethod
    def setUpClass(cls):
        # トランザクションを開始するため、必ず親クラスのsetUpClass()を最初に呼ぶこと
        super().setUpClass()
        # ログインユーザーを初期登録
        cls.user = get_user_model().objects.create_user(
            username='user',
            email='user@example.com',
            password='secret',
        )

    def test_update_success(self):
        """本モデルの更新APIへのPUTリクエスト（正常系）"""

        # ログイン（Cookie認証の場合）
        # self.client.login(username='user', password='secret')
        # ログイン（JWT認証の場合）
        token = str(RefreshToken.for_user(self.user).access_token)
        self.client.credentials(HTTP_AUTHORIZATION='JWT ' + token)

        # APIリクエストを実行
        book = Book.objects.create(
            title='aaa',
            price=111,
        )
        params = {
            'id': book.id,
            'title': 'bbb',
            'price': 222,
        }
        response = self.client.put(
            self.TARGET_URL_WITH_PK.format(book.id), params, format='json',
        )

        # レスポンスの内容を検証
        self.assertEqual(response.status_code, 200)
        book = Book.objects.get()
        expected_json_dict = {
            'id': str(book.id),
            'title': params['title'],
            'price': params['price'],
            'created_at': str(localtime(book.created_at)).replace(' ', 'T'),
        }
        self.assertJSONEqual(response.content, expected_json_dict)
