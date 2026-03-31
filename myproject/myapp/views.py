from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm, BookForm, RecordForm, ReturnRecordForm
from .models import User, Book, Record


# Dashboard
def dashboard(request):
    context = {
        'users_count': User.objects.count(),
        'books_count': Book.objects.count(),
        'open_records_count': Record.objects.filter(status='open').count(),
        'closed_records_count': Record.objects.filter(status='closed').count(),
    }
    return render(request, 'dashboard.html', context)

# Users

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users': users})


def add_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        # Status is assigned internally when creating a user!!!
        form.fields['status'].required = False
        if form.is_valid():
            user = form.save(commit=False)
            user.status = 1     # Active User (newly added!!)
            user.save()
            return redirect('users')
    else:
        form = UserForm()

    return render(request, 'add_user.html', {'form': form})


def edit_user(request, id):
    user = User.objects.get(id=id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        form.fields['status'].required = False
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
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
    return render(request, 'book_details.html', {'book': book})


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
    if request.method != 'POST':
        return redirect('open_records')

    record = get_object_or_404(Record, id=id, status='open')
    form = ReturnRecordForm(request.POST, instance=record)
    if form.is_valid():
        returned_record = form.save(commit=False)
        returned_record.status = 'closed'
        returned_record.save()
    return redirect('open_records')


def open_records(request):
    records = Record.objects.filter(status='open')
    context = {
        'open_records': records,
        'return_form': ReturnRecordForm(),
    }
    return render(request, 'open_records.html', context)


def closed_records(request):
    records = Record.objects.filter(status='closed')
    return render(request, 'closed_records.html', {'closed_records': records})


def record_detail(request, id):
    record = Record.objects.get(id=id)
    return render(request, 'record_details.html', {'record': record})