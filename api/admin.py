from django.contrib import admin

from .models import Publisher, Author, Book, BookStock


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
    ordering = ('created_at',)


admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book, BookAdmin)
admin.site.register(BookStock)
