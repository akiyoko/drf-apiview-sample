from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views as api_view
from apiv1 import views as apiv1_view
from apiv2 import views as apiv2_view

router = routers.DefaultRouter()
router.register('books', apiv2_view.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', api_view.BookListCreateAPIView.as_view()),
    path('api/books/<pk>/', api_view.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books/', apiv1_view.BookListCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', apiv1_view.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v2/', include(router.urls)),
]
