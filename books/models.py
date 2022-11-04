from django.db import models
from users.models import User


class Book(models.Model):
    class Meta:
        db_table = "book"

    title = models.CharField(max_length=1200, primary_key=True)
    author = models.CharField(max_length=1000, null=True)
    publisher = models.CharField(max_length=1000, null=True)
    pub_date = models.CharField(max_length=10, null=True)
    img_url = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    interest = models.ManyToManyField(User, related_name='interest_book')
    life = models.ManyToManyField(User, related_name='life_book')

    def __str__(self):
        return self.title


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="review")
    title = models.TextField(max_length=30)
    content = models.TextField(min_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return str(self.content)