from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    user = models.ForeignKey(User, related_name='tasks', on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, related_name='tasks')

    def __str__(self):
        return self.title
