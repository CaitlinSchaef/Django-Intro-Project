from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    # I'm leaving the published date as a CharField, but if I was just doing digits it could be PositiveIntegerField()
    #Book had to go under author, because book is the many and author is the one

class Reader(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

