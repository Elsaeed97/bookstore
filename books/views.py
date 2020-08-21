from django.shortcuts import render
from .models import Book
# Create your views here.

def book_list(request):
	books = Book.objects.all()
	context ={
		'books':books
	}
	return render(request, 'books/book_list.html',context)

def book_detail(request, pk):
	book = Book.objects.get(id=pk)
	context = {
		'book':book,

	}
	return render(request,'books/book_detail.html', context)
