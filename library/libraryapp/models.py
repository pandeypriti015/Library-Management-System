from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
import datetime

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_publisher = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)
    book_stock = models.IntegerField(default=1)

    def __str__(self):
        return self.book_name

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)
    student_number = models.IntegerField()
    book_name = models.ForeignKey(Book,'on_delete=models.CASCADE')
    date_of_issue = models.DateField(auto_now_add=True)
    date_of_return = models.DateField(datetime.datetime.today()+datetime.timedelta(days=7))

    def __str__(self):
        return self.student_name

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.author_id


class Barrower(models.Model):
    id = models.AutoField(primary_key=True)
    card = models.ForeignKey(Student,'on_delete=model.CASCADE')
    book = models.ForeignKey(Book,'on_delete=model.CASCADE')
    issue_date = models.DateField(null=True)
    due_date = models.DateField(null=True)
    date_return = models.DateField(null=True)
    availability = models.BooleanField()

    def __str__(self):
        return self.id

class Record(models.Model):
    name = models.ForeignKey(Student,'on_delete=model.CASCADE')
    book = models.ForeignKey(Book,'on_delete=models.CASCADE')
    date_issue = models.DateField(null=True)
    date_return = models.DateField(null=True)
    availability = models.BooleanField()

    def __str__(self):
        return self.book


#class check(models.Model):

@receiver(post_save,sender=Barrower)
def update_stock(sender,instance,**kwargs):
    instance.book.BookInstance -= instance.avalibility
    instance.post.save()


