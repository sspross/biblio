from django.contrib import admin

from biblio.models import Book, Author, Publisher


class BookAdmin(admin.ModelAdmin):
    list_display = ('num', 'opan', 'isbn', 'title', 'author', 'publisher', 'year',)
    search_fields = ('num', 'opan', 'isbn', 'title', 'author', 'publisher', 'year',)
    readonly_fields = tuple()
    raw_id_fields = ('author', 'publisher',)


admin.site.register(Book, BookAdmin)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname',)
    search_fields = ('lastname', 'firstname',)


admin.site.register(Author, AuthorAdmin)


class PublisherAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Publisher, PublisherAdmin)
