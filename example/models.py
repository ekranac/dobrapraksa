from django.db import models

class Example(models.Model):
    title=models.charField(max_length=20)
    content=models.textField()
    author=ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    approved=models.BooleanField(default=False)

class User(models.Model):
    first_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.CharField(max_length=20)

class Comment(models.Model):
    author=models.ForeignKey(User)
    date=models.DateTimeField(auto_now_add=True)
    content=models.textField()