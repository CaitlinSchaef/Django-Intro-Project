from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'AUTHOR NAME: {self.name}'
    
class Book(models.Model):
    title = models.CharField(max_length=100)
    published_date = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    #Book had to go under author, because book is the many and author is the one
    def __str__(self):
        return f'TITLE: {self.title}, PUBLICATION DATE: {self.published_date}' # AUTHOR: {self.author}

class Reader(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    books = models.ManyToManyField(Book)

    def __str__(self):
        return f'READER NAME: {self.name}, STATE: {self.state}'
