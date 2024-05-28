from django.shortcuts import render, get_object_or_404
from .models import Post, Tag
from .forms import CommentForm
from django.core.paginator import Paginator
from django.db.models import Q


def post_list(request, tag_slug=None):
    posts = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, name=tag_slug)
        posts = posts.filter(tags__in=[tag])

    query = request.GET.get("q")
    if query:
        posts = posts.filter(Q(title__icontains=query) | Q(content__icontains=query))

    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(
        request, "blog/post_list.html", {"posts": page_obj, "tag": tag, "query": query}
    )


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        "blog/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
