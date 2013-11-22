from django.shortcuts import render, get_object_or_404
from example.models import Example, Comment

def post(request, slug):
    post=get_object_or_404(Example, slug=slug)
    comment_list=Comment.objects.filter(example=post)
    return render(request, 'example.html', {'post':post, "comment_list":comment_list})

def index(request):
    post_list=Example.objects.filter(approved=True)
    return render(request, 'index.html', {"posts":post_list})
'''
def comment(request):
'''