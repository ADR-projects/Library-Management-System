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
        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')

            if User.objects.filter(email=email).exists():
                self.add_error("User with this Email already exists!")

            return cleaned_data


# Book Form (Add + Edit)
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


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
        open_user_ids = Record.objects.filter(status='open').values_list('user_id', flat=True)
        self.fields['user'].queryset = User.objects.exclude(id__in=open_user_ids)

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