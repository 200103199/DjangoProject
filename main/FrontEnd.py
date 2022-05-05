from django.db import models

class task(models.Model):
    title = models.CharField(max_length=255)
    tasks = models.TextField(max_length=100,default=" ")

class data(models.Model):
    name = models.CharField(max_length=100)

class Test(models.Model):
    hobby = models.CharField(max_length=100)

class Database(models.Model):
    title = models.CharField(max_length=100)
    database= models.TextField(max_length= 100)
class Book(models.Model):
    name = models.CharField(max_length = 50)
    author = models.CharField(max_length = 30)
    email = models.EmailField(blank = True)
    describe = models.TextField()
    def __str__(self):
        return self.name

class Posts(models.Model):
    title=models.CharField(max_length=255, verbose="Takyryp")
    is_published = models.BooleonField(default=True,verbose_name = "shygarylym")

        
