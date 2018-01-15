from django.contrib import admin
from.models import *
# Register your models here.


class BooksAdmin(admin.ModelAdmin):
    fields = ('name_book', 'price_book')
    list_filter = ('name_book', 'price_book')
    list_display = ('name_book', 'price_book')
    search_fields = ('name_book', 'price_book')
    list_per_page = 10


class WritersAdmin(admin.ModelAdmin):
    fields = ('writer_fio', 'writer_book')
    list_filter = ('writer_fio', 'writer_book')
    list_display = ('writer_fio', 'writer_book')
    search_fields = ('writer_fio', 'writer_book')
    list_per_page = 10


admin.site.register(Book, BooksAdmin)
admin.site.register(Writer, WritersAdmin)
admin.site.site_url = '/main/'
admin.site.site_header = 'Django Администрирование'
admin.site.index_title = 'Администрирование'
