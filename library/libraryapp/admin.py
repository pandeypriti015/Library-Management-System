from django.contrib import admin

# Register your models here.
from .models import Book,Member,Author,Borrows
from django import forms

class AuthorForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(AuthorForm,self).__init__(*args,**kwargs)

    def clean(self):
        author_name = self.cleaned_data.get('author_name')
        if len(author_name) < 4:
            raise forms.ValidationError("Name is too short",code="invalid")

        return self.cleaned_data

class AuthorAdmin(admin.ModelAdmin):
    form = AuthorForm

class BookForm(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BookForm,self).__init__(*args,**kwargs)

    def clean(self):
        book_name =self.cleaned_data.get('book_name')
        if len(book_name)< 10:
            raise forms.ValidationError("Name is too short",code="invalid")

        return self.cleaned_data

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name','book_publisher','book_author',
                    'in_stock','availability','number_of_copy','book_discription',)
    search_fields = ('book_name','book_author',)
    list_filter = ('availability',)
    ordering = ('book_name',)

    form = BookForm

class BorrowAdminform(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super(BorrowAdminform,self).__init__(*args,**kwargs)

    def clean(self):
        borrowed_book = self.cleaned_data.get('borrowed_book')
        if borrowed_book.in_stock == 0:
            raise forms.ValidationError("Book is not available.", code="invalid")

        return self.cleaned_data

    def save(self,commit=True):
        return super(BorrowAdminform,self).save(commit)

class BorrowerAdmin(admin.ModelAdmin):
    list_display = ('borrowed_member','borrowed_book','borrowed_date','book_returned','return_date',)
    list_filter =('return_date',)
    search_fields = ('borrowed_member_member_name','borrowed_name','borrowed_number_member_id',)
    ordering = ('return_date',)

    form = BorrowAdminform

class MemberAdminForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super(MemberAdminForm,self).__init__(*args,**kwargs)
    def clean(self):
        member_name=self.cleaned_data.get('member_name')
        if len(member_name)<10:
            raise forms.ValidationError("Name is short",code= "invalid")
        return self.cleaned_data


class MemberAdmin(admin.ModelAdmin):
    list_display = ('member_id','member_name','member_address',
                    'member_phone_no','member_email',)
    ordering = ('member_name',)
    form = MemberAdminForm

admin.site.register(Book,BookAdmin)
admin.site.register(Member,MemberAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Borrows,BorrowerAdmin)

