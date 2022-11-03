from django.db import models

# Create your models here.
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
    
    def __str__(self):
        return self.title