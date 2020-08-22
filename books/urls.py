from django.urls import path
from .views import book_list,BookDetailView
urlpatterns =[
	path('<uuid:pk>/', BookDetailView.as_view() , name='book_detail'),
	path('', book_list, name='book_list' ),
]