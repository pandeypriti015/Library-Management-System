from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    book_publisher = models.CharField(max_length=200)
    book_author = models.CharField(max_length=200)

    def __str__(self):
        return self.book_name + str(self.book_publisher) + str(self.book_author)

class Student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_name = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)
    student_number = models.IntegerField()
    book_name = models.ForeignKey(Book,'on_delete=models.CASCADE')
    date_of_issue = models.DateField()
    date_of_return = models.DateField()

    def __str__(self):
        return self.student_name

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    author_name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.author_id

