from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api import views as api_views
from apiv1 import views as apiv1_views
from apiv2 import views as apiv2_views

router = routers.DefaultRouter()
router.register('books', apiv2_views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/books/', api_views.BookListCreateAPIView.as_view()),
    path('api/books/<pk>/', api_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books/', apiv1_views.BookListCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', apiv1_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v2/', include(router.urls)),
]
