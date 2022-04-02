from django.urls import path
from . import views

urlpatterns = [
    path('book_list/', views.BookListView.as_view(), name='book_list'),
    path('book_detail/<int:book_id>', views.BookDetailView.as_view(), name='book_detail'),
    path('book_by_author_id/<int:author_id>', views.BookByAuthorView.as_view(), name='book_by_author_id'),
    path('book_unordered_list/', views.BookUnorderedListView.as_view(), name='book_unordered_list'),
    path('book_list/book_list_asc', views.BookListOrderedAsc.as_view(), name='book_list/book_list_asc'),
    path('book_list/book_list_desc', views.BookListOrderedDesc.as_view(), name='book_list/book_list_desc'),
    path('book_list/book_list_count', views.BookListOrderedCount.as_view(), name='book_list/book_list_count')
]
