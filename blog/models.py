from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=200)


class Post(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description=models.TextField(blank=True,null=True)
