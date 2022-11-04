from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = "book"
        
    #csv파일 DB전송시 중복된 도서가 올라가지 않도록 title을 primary키로 지정
    title = models.CharField(max_length=1200, primary_key=True)
    author = models.CharField(max_length=1000, null=True)
    publisher = models.CharField(max_length=1000, null=True)
    pub_date = models.CharField(max_length=10, null=True)
    img_url = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    category = models.CharField(max_length=5, null=True)
    
    def __str__(self):
        return self.title