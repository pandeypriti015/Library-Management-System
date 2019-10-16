from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from datetime import date,timedelta
from django.db.models import signals

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_publisher = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    in_stock = models.IntegerField(default=1)
    availability =models.BooleanField(default=False)
    number_of_copy =models.IntegerField(default=1)
    book_discription = models.TextField(blank=True,null=True)


    def __str__(self):
        return self.book_name

    def get_title(self):
        return self.book_name

class Member(models.Model):
    member_id = models.CharField(max_length=6)
    member_name = models.CharField(max_length=100)
    member_address = models.CharField(max_length=200)
    member_phone_no = models.IntegerField()
    member_email = models.EmailField()


    def __str__(self):
        return self.member_name


class Author(models.Model):
    author_name = models.CharField(max_length=100)
    author_address = models.CharField(max_length=100)

    def __str__(self):
        return self.author_name

    def get_title(self):
        return self.author_name

class Borrows(models.Model):
    borrowed_member= models.ForeignKey(Member,on_delete=models.CASCADE)
    borrowed_book = models.ForeignKey(Book,on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    book_returned = models.BooleanField(auto_created=True, default=False)
    return_date =models.DateField(default= date.today()+timedelta(days=7))

    def expired(self):
        return_date = self.return_date
        if date.today()>return_date:
            return True
        else:
            return False

    def is_returned(self):
        if self.book_returned:
            return True
        else:
            return False

    is_returned.boolean = True
    is_returned.short_description= 'Returned'
    expired.boolean=True
    expired.short_description= 'Expired'



@receiver(post_save,sender = Borrows)
def update_stock(sender,instance,created,**kwargs):
    stock = instance.borrowed_book.in_stock
    if not instance.book_returned:
        if instance.borrowed_book.number_of_copy >= stock:
            stock +=1
            book = instance.borrowed_book
            instance.book_returned = True
            book.in_stock = stock
            if stock > 0:
                book.availability = True
            book.save()



@receiver(signals.post_save,sender = Borrows)
def is_barrowed(sender,instance,created,**kwargs):
    if not instance.book_returned:
        if created:
            stock = instance.borrowed_book.in_stock
            if stock > 0:
                stock -= 1
                book = instance.borrowed_book
                book.in_stock = stock
                if stock <= 0:
                    book.availability = False
                book.save()
    else:
        stock = instance.borrowed_book.in_stock
        book = instance.borrowed_book
        book.in_stock = stock+1
        book.save()
