from django.db import models
from django.utils.text import slugify

# Create your models here
class Category(models.Model):
     category = models.CharField(max_length=100)

     def __str__(self):
       return self.category


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    img = models.URLField(max_length=4000)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def save(self,*args, **kwargs):
         self.slug = slugify(self.title)
         super().save(*args, **kwargs)

    def __str__(self):
         return self.title

     
