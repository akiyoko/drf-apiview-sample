from django.contrib import admin
from django.urls import path

from api import views as api_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', api_view.BookListCreateAPIView.as_view()),
    path('api/books/<pk>/', api_view.BookRetrieveUpdateDestroyAPIView.as_view()),
]
