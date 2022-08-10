from distutils.command.upload import upload
from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify


class Post(models.Model):
    post_name = models.CharField(max_length=223)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(auto_now_add=True)
    
class Images(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE,null=True, blank=True,related_name='images')
    images = models.ImageField(upload_to='images/')

def __str__(self):
    return self.post.post_name


def __str__(self):
    return self.post_name




