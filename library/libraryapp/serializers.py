from rest_framework import serializers
from .models import Book,Member,Author,Borrows

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields =('id', 'book_name','book_publisher','book_author','in_stock',
                 'availability','number_of_copy','book_discription',)


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields =('member_id','member_name','member_address','member_phone_no','member_email',)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('author_name','author_address',)


class BorrowsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrows
        fields =('borrowed_member','borrowed_book','borrowed_date','book_returned','return_date',)



