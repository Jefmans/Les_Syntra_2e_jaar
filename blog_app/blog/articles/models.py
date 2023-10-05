from django.db import models

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name

class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()

    creation_date = models.DateTimeField(auto_created=True)

    def __str__(self) -> str:
        return self.title