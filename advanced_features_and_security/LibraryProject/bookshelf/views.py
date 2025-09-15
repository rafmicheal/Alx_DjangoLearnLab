from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from .models import Book, Author

# View all books - requires can_view permission


@permission_required('bookshelf.can_view', raise_exception=True)
def view_books(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/view_books.html', {'books': books})

# Create a book - requires can_create permission


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author_id = request.POST.get('author')
        author = Author.objects.get(id=author_id)
        Book.objects.create(title=title, author=author)
        return redirect('view_books')
    authors = Author.objects.all()
    return render(request, 'bookshelf/create_book.html', {'authors': authors})

# Edit a book - requires can_edit permission


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.save()
        return redirect('view_books')
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Delete a book - requires can_delete permission


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('view_books')
    return render(request, 'bookshelf/delete_book.html', {'book': book})
