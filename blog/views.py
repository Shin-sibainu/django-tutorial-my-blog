from django.shortcuts import redirect, render
from .models import Post
from .forms import CommentForm


def frontpage(request):
    posts = Post.objects.all()
    return render(request, "blog/frontpage.html", {"posts": posts})


def post_detail(request, slug):
    # print(slug) #post-1, post-2
    post = Post.objects.get(slug=slug)
    # print(post) #Post Object (2)
    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()

            return redirect("post_detail", slug=post.slug)

    else:
        form = CommentForm()

    return render(request, "blog/post_detail.html", {"post": post, "form": form})
