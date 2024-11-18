from django.db import models
from categories.models import Category
# from author.models import Author
# Create your models here.
from django.contrib.auth.models import User
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    category = models.ManyToManyField(Category) # many to many relationship in posts and categories
    author = models.ForeignKey(User, on_delete=models.CASCADE) # many to one relationship

    def __str__(self):
        return self.title