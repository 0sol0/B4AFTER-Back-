from django.db import models

# Create your models here.
class Book(models.Model):
    class Meta:
        db_table = "book"
        
    #csv파일 DB전송시 중복된 도서가 올라가지 않도록 title을 primary키로 지정
<<<<<<< HEAD
    title = models.CharField(max_length=1200, primary_key=True) # 제목
    author = models.CharField(max_length=1000, null=True) # 저자
    publisher = models.CharField(max_length=1000, null=True) # 출판사
    pub_date = models.CharField(max_length=10, null=True) # 발행일자
    img_url = models.CharField(max_length=1000, null=True) # 이미지
    description = models.TextField(null=True)           # 책소개
    isbn13 = models.CharField(max_length=13, null=True) # isbn
=======
    title = models.CharField(max_length=1200, primary_key=True)
    author = models.CharField(max_length=1000, null=True)
    publisher = models.CharField(max_length=1000, null=True)
    pub_date = models.CharField(max_length=10, null=True)
    img_url = models.CharField(max_length=1000, null=True)
    description = models.TextField(null=True)
    isbn13 = models.CharField(max_length=13, null=True)
    category = models.CharField(max_length=5, null=True)
>>>>>>> 3d8ce18c359b319b152708426004045f2f77bcc1
    
    def __str__(self):
        return self.title