from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'Author',
        on_delete=models.CASCADE,
    )
    publication  = models.ForeignKey('Publication',on_delete=models.CASCADE, default = 1)
    status = models.BooleanField(default=True)

    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name

class Publication(models.Model):
    name = models.CharField(max_length=200)
    status = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name