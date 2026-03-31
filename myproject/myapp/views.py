from django.shortcuts import render, redirect
from .forms import UserForm, BookForm, RecordForm
from .models import User, Book, Record


# Dashboard
def dashboard(request):
    return render(request, 'dashboard.html')

# Users

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def edit_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm(instance=user)

    return render(request, 'edit_user.html', {'form': form})


def delete_user(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('users')


def user_detail(request, id):
    user = User.objects.get(id=id)
    return render(request, 'user_detail.html', {'user': user})


# Books

def books(request):
    books = Book.objects.all()
    return render(request, 'books.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def edit_book(request, id):
    book = Book.objects.get(id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm(instance=book)

    return render(request, 'edit_book.html', {'form': form})


def delete_book(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    return redirect('books')


def book_detail(request, id):
    book = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {'book': book})


# Records

def borrow_book(request):
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('open_records')
    else:
        form = RecordForm()

    return render(request, 'borrow_book.html', {'form': form})


def return_book(request, id):
    record = Record.objects.get(id=id)
    record.status = 'closed'
    record.return_date = record.return_date or record.issue_date  # simple placeholder
    record.save()
    return redirect('open_records')


def open_records(request):
    records = Record.objects.filter(status='open')
    return render(request, 'open_records.html', {'open_records': records})


def closed_records(request):
    records = Record.objects.filter(status='closed')
    return render(request, 'closed_records.html', {'closed_records': records})


def record_detail(request, id):
    record = Record.objects.get(id=id)
    return render(request, 'record_detail.html', {'record': record})