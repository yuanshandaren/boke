from django.db import models
from django.contrib.auth.models import User
# Create your models here.
#class Author(models.Model):
#    name = models.CharField(max_length=30)
#    email = models.EmailField(blank=True)
#    website = models.URLField(blank=True)
#    def __str__(self):
#        return self.name

class Post(models.Model):
    Post_text = models.TextField(max_length=200)
    title = models.CharField(max_length=30)
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User)


