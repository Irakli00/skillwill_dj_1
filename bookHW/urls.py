
from django.contrib import admin
from django.urls import path

from book.views import books_collection
from reader.views import reader_input

urlpatterns = [
    path('admin/', admin.site.urls),
    path('log_in/',reader_input, name='reader_input'),
    path('books/',books_collection,name='books')
]
