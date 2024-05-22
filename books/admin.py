from django.contrib import admin

from .models import Books, Reviews

class ReviewsInline(admin.TabularInline):
    model = Reviews

class BooksAdmin(admin.ModelAdmin):
    inlines = [
        ReviewsInline,
    ]
    list_display = ('title', 'author', 'price')

admin.site.register(Books, BooksAdmin)

