from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.db.models import Q

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
    queryset = Books.objects.all().prefetch_related('reviews__author',)

class SearchResultsView(ListView):
    model = Books
    context_object_name = 'book_list'
    template_name = 'books/search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Books.objects.filter(
            Q(title__icontains=query) | Q(author__icontains=query)
        )