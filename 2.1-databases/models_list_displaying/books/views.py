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

def books_view_by_pub_date(request, pub_date:str):
    """
    Функция показывает список книг из БД по дате публикации

    """
    template = 'books/filtred_books_list.html'
    all_books = Book.objects.all().order_by('pub_date') #для последующего формирования списка дат
    filtred_books = Book.objects.filter(pub_date=pub_date)

    # формируем список дат
    pub_dates_list = []
    for book in all_books:
        pub_dates_list.append(str(book.pub_date))

    # в зависимости от индекса pub_date в списке всех дат
    # формируем переменные next_date и prev_date
    num_pub_date_in_list = pub_dates_list.index(pub_date)
    if num_pub_date_in_list == 0:
        next_date = pub_dates_list[1]
        prev_date = None
    elif  num_pub_date_in_list == len(pub_dates_list) - 1:
        prev_date = pub_dates_list[num_pub_date_in_list - 1]
        next_date = None
    else:
        next_date = pub_dates_list[num_pub_date_in_list + 1]
        prev_date = pub_dates_list[num_pub_date_in_list - 1]

    context = {
        'books': filtred_books,
        'pub_date': pub_date,
        'prev_date': prev_date,
        'next_date': next_date,
    }
    return render(request, template, context)
