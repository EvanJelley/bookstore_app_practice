from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from .models import Books

class BookListView(LoginRequiredMixin, ListView):
    model = Books
    template_name = 'books/book_list.html'
    context_object_name = 'books'
    login_url = 'account_login'

class BookDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Books
    template_name = 'books/book_detail.html'
    context_object_name = 'book'
    login_url = 'account_login'
    permission_required = 'books.special_status'
