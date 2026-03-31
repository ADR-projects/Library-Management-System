from django.db import models
from django.utils import timezone

# Create your models here.
status_choices = [
    (0, 'Inactive'),
    (1, 'Active'),
    (5, 'Delete')
]
class User(models.Model):
    name = models.CharField(max_length = 100)
    email = models.EmailField(max_length = 100)
    phone = models.CharField(max_length = 100)
    address = models.CharField(max_length = 100)
    status = models.IntegerField(choices = status_choices, default = 1)

    class Meta:
        db_table = 'user_table'

    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    stock = models.IntegerField()

    class Meta:
        db_table = 'book_table'

    def __str__(self):
        return self.title

class Record(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)

    status = models.CharField(max_length=10, default='open')  
    # values: 'open' (not returned), 'closed' (returned)

    issue_date = models.DateField(default=timezone.now)
    # can be selected while borrowing; defaults to now if omitted

    return_date = models.DateField(null=True, blank=True)  
    # null = not returned yet 

    class Meta:
        db_table = 'record_table'


    def __str__(self):
        return f"{self.user} - {self.book} ({self.status})"

     
