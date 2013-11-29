from django.shortcuts import render, get_object_or_404
from example.models import Example, Comment
from django.http import HttpResponseRedirect

def post(request, slug):
    post=get_object_or_404(Example, slug=slug)
    return render(request, 'example.html', {'post':post})

def index(request):
    post_list=Example.objects.filter(approved=True)
    return render(request, 'index.html', {"posts":post_list})