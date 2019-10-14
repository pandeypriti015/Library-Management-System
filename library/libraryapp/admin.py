from django.contrib import admin

# Register your models here.
from .models import Book,Student,Author

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_publisher','book_author',)
    search_fields = ('book_name','book_author',)
    ordering = ('book_name','book_publisher',)
admin.site.register(Book,BookAdmin)
