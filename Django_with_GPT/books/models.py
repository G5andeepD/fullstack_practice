from django.db import models
from django.core.validators import RegexValidator

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    publication_date = models.DateField()
    isbn = models.CharField(max_length=20, unique=True)
    genre = models.CharField(max_length=50)


