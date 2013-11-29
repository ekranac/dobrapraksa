from django.db import models
from django.contrib.auth.models import User

class Example(models.Model):
    title=models.CharField(max_length=20)
    description=models.CharField(max_length=50)
    content=models.TextField()
    author=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)
    slug=models.SlugField(unique=True, max_length=255)

    def get_absolute_url(self):
        return self.slug

class Comment(models.Model):
    author=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    content=models.TextField()
    example=models.ForeignKey(Example)