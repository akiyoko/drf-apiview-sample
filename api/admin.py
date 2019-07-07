from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    ordering = ('created_at',)


admin.site.register(Book, BookAdmin)
