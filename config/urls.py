from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.documentation import include_docs_urls

from api import views
from apiv1 import views as apiv1_views
from apiv2 import views as apiv2_views

router = routers.DefaultRouter()
router.register('books', apiv2_views.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/books/', views.BookListCreateAPIView.as_view()),
    path('api/books/<pk>/', views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v1/books/', apiv1_views.BookListCreateAPIView.as_view()),
    path('api/v1/books/<pk>/', apiv1_views.BookRetrieveUpdateDestroyAPIView.as_view()),
    path('api/v2/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += [path('docs/', include_docs_urls(title='APIドキュメント'))]
