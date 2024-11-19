from django.db import models
# Create your models here.
#this step should create a table in our db
class Task(models.Model):
    title = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    author = models.CharField(max_length=100)
    published_date = models.DateField()

    def __str__(self):
        return self.title
