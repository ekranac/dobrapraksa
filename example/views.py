from django.shortcuts import render, get_object_or_404
from example.models import Example

def post(request, slug):
    post=get_object_or_404(Example, slug=slug)
    return render(request, 'example.html', {'post':post})