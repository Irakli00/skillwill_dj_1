from django.shortcuts import render

def books_collection(request):
    book1 = {'name': 'book-1', 'author': 'A.A'}
    book2 = {'name': 'book-2', 'author': 'B.B'}
    book3 = {'name': 'book-3', 'author': 'C.C'}
    book4 = {'name': 'book-4', 'author': 'D.D'}
    book5 = {'name': 'book-5', 'author': 'E.E'}

    books = [book1,book2,book3,book4,book5]
    #books = []

    return render(request,'books.html',{'data':books})
