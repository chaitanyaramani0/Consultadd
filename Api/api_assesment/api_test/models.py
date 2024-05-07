from django.db import models

# Create your models here.

class Catagory(models.Model):
    category = models.CharField(max_length=1000)

    def __str__(self):
        return self.category
    
class Author(models.Model):
    name  = models.CharField(max_length=256,null=True, blank=True)
    country = models.CharField(max_length=256,null=True, blank=True)

    def __str__(self):
        return self.name

class Books(models.Model):
    name = models.CharField(max_length=256,blank=True,null=True)
    price = models.IntegerField(blank=True,null=True)
    discription = models.TextField(max_length=1000,blank=True,null=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =  ['created']

    def __str__(self):
        return self.name
    