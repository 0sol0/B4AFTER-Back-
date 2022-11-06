from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = "book"
        
    #csv파일 DB전송시 중복된 도서가 올라가지 않도록 ISBN을 primary키로 지정
    isbn = models.CharField(max_length=13, primary_key=True)
    book_title = models.CharField(max_length=1000, null=True)
    book_author = models.CharField(max_length=1000, null=True)
    year_of_publication = models.CharField(max_length=10, null=True)
    book_publisher = models.CharField(max_length=1000, null=True)
    img_l = models.CharField(max_length=1000, null=True)
    summary = models.CharField(max_length=13, null=True)
    category = models.CharField(max_length=100, null=True)

    
    def __str__(self):
        return self.title