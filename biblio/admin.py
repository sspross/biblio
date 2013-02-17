from django.contrib import admin

from biblio.models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('num', 'opan', 'isbn', 'title',)
    search_fields = ('num', 'opan', 'isbn', 'title',)
    readonly_fields = ('title',)


admin.site.register(Book, BookAdmin)
