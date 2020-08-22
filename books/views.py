from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import (LoginRequiredMixin,PermissionRequiredMixin)
from django.views.generic import ListView, DetailView


# Create your views here.

@login_required
def book_list(request):
	books = Book.objects.all()
	context ={
		'books':books
	}
	return render(request, 'books/book_list.html',context)

# @login_required
# def book_detail(request, pk):
# 	book = Book.objects.get(id=pk)
# 	context = {
# 		'book':book,

# 	}
# 	return render(request,'books/book_detail.html', context)

class BookDetailView(LoginRequiredMixin,PermissionRequiredMixin, DetailView):
	model = Book
	context_object_name = 'book'
	template_name = 'books/book_detail.html'
	login_url = 'account_login'
	permission_required = 'books.special_status' 