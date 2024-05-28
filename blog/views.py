from django.shortcuts import render, get_object_or_404
from .models import Post


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    print("detail post")
    post = get_object_or_404(Post, id=post_id)
    return render(request, "blog/post_detail.html", {"post": post})
