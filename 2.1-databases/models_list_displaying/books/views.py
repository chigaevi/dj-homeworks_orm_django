from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from books.models import Book

def index(request):
    return redirect('books')

def books_view(request):
    template = 'books/books_list.html'
    books = Book.objects.all()

    context = {
        'books': books,
    }
    return render(request, template, context)

def books_view_by_pub_date(request, pub_date):
    all_books = Book.objects.all()

    print(books)
    date_list = []
    for book in books:
        date_list.append(book.pub_date)
    paginator = Paginator(date_list)
