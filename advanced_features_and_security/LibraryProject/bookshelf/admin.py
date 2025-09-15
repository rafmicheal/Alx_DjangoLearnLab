from django.shortcuts import render, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# View to list all books


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# View to create a new book


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('book_list')

    authors = Author.objects.all()
    return render(request, 'bookshelf/create_book.html', {'authors': authors})

# View to edit a book


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        author_id = request.POST.get('author')
        book.author = Author.objects.get(id=author_id)
        book.save()
        return redirect('book_list')

    authors = Author.objects.all()
    return render(request, 'bookshelf/edit_book.html', {'book': book, 'authors': authors})

# View to delete a book


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('book_list')
