from django.contrib import admin

# Register your models here.
from .models import Book,Student,Author,Barrower,Record


class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_publisher','book_author',)
    search_fields = ('book_name','book_author',)
    ordering = ('book_name',)


class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id','student_name','student_address',
                    'student_number','book_name','date_of_issue','date_of_return',)
    ordering = ('student_name',)


class BarrowerAdmin(admin.ModelAdmin):
    list_display = ('id','card','issue_date','due_date','date_return','availability',)
    ordering = ('due_date',)


class RecordAdmin(admin.ModelAdmin):
    list_display = ('name','book','date_issue','date_return','availability',)
    ordering = ('book',)





admin.site.register(Book,BookAdmin)


admin.site.register(Student,StudentAdmin)


admin.site.register(Barrower,BarrowerAdmin)

admin.site.register(Record,RecordAdmin)