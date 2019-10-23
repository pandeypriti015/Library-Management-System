from django.test import TestCase
from .models import Author,Book


#  Create your tests here.

class AuthorTestCase(TestCase):
    def setUp(self):
        Author.objects.create(author_name="BrettMard")
        Author.objects.create(author_name="Willey")

    def test_case_author_Correct_Tittle(self):
        brettmard = Author.objects.get(author_name="BrettMard")
        willey = Author.objects.get(author_name="Willey")
        self.assertEqual(brettmard.get_title(), "BrettMard")
        self.assertEqual(willey.get_title(), "Willey")



class BookTestCase(TestCase):
    def sutUp(self):
        author = Author.objects.create(author_name="brettmard")
        Book.objects.create(book_name="Python", book_publisher="Willy")

    def test_case_get_book_details(self):
        book = Book.objects.get(book_name="Python",book_publisher="Willey")
        author = Author.objects.get(author_name="brettmard")


        self.asserEqual(book.get_tittle(), "Python", "Willey")
        self.assertEqual(author.get_author(), "brettmard")
