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
    title=models.CharField(max_length=255, verbose_name="Takyryp")
    is_published = models.BooleanField(default=True, verbose_name = "shygarylym")

class Category(models.Model):
    category_description = models.CharField(max_length=5000)

    def __str__(self):
        return self.category_description

class Book(models.Model):
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year = models.IntegerField(null=True)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.category_id

class Author(models.Model):
    author_name = models.CharField(max_length=200)

class Author_Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE, null=True)

class Customer(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)

class Book_Order(models.Model):
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True)
    order_date = models.DateField()

class Ordering(models.Model):
    order = models.ForeignKey('Book_Order', on_delete=models.CASCADE, null=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=True)
        
