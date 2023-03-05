from datetime import datetime

from django.core.paginator import Paginator
from django.http import HttpResponse
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
    template = 'books/filtred_books_list.html'
    all_books = Book.objects.all()
    fitred_books = Book.objects.filter(pub_date=pub_date)
    pub_dates_list = []
    for book in all_books:
        pub_dates_list.append(str(book.pub_date))
    pub_dates_list = list(set(pub_dates_list))
    print(pub_dates_list)
    num_date = pub_dates_list.index(pub_date)
    print(num_date)
    if num_date == 0:
        next_date = pub_dates_list[1]
        prev_date = None
    elif  num_date == len(pub_dates_list) - 1:
        prev_date = pub_dates_list[num_date - 1]
        next_date = None
    else:
        next_date = pub_dates_list[num_date + 1]
        prev_date = pub_dates_list[num_date - 1]



    context = {
        'books': fitred_books,
        'pub_date': pub_date,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)