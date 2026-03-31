from django import forms
from .models import User, Book, Record


# User Form (Add + Edit)
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter Email'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Enter Phone'}),
            'address': forms.Textarea(attrs={'placeholder': 'Enter Address'}),
        }


# Book Form (Add + Edit)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'book_name': forms.TextInput(attrs={'placeholder': 'Enter Book Name'}),
            'author': forms.TextInput(attrs={'placeholder': 'Enter Author'}),
            'stock': forms.NumberInput(attrs={'placeholder': 'Enter Stock'}),
        }


# Borrow Book Form (Create Record)
class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['user', 'book', 'issue_date']

        labels = {
            'user': 'Select User',
            'book': 'Select Book',
            'issue_date': 'Issue Date'
        }

        widgets = {
            'issue_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['issue_date'].input_formats = ['%Y-%m-%d']

class ReturnRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['return_date']
        labels = {
            'return_date': 'Return Date'
        }
        widgets = {
            'return_date': forms.DateInput(
                attrs={'type': 'date'}
            )
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['return_date'].input_formats = ['%Y-%m-%d']