from django.template.loader import get_template
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from example.forms import CreateCommentForm
from example.models import Example, Comment, User
from django.http import HttpResponseRedirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required


@login_required
def post(request, slug):
    post=get_object_or_404(Example, slug=slug)
    comment_list=Comment.objects.filter(example=post)
    form=CreateCommentForm(request.POST)

    if form.is_valid():
           comment=form.save(commit=False)
           comment.example=post
           comment.author=request.user
           form.save(commit=True)

           return HttpResponseRedirect("/%s" % post.slug)
    else:
        form=CreateCommentForm()

    return render(request, "example.html", {"post":post, "comment_list":comment_list, "form":form})

def index(request):
    post_list=Example.objects.filter(approved=True)
    return render(request, 'index.html', {"posts":post_list})