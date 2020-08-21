from django.urls import path
from .views import book_list,book_detail
urlpatterns =[
	path('<uuid:pk>/', book_detail, name='book_detail'),
	path('', book_list, name='book_list' ),
]