from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from my_blog.models import Post, Comment
from .forms import PostForm, CommentForm


def post_detail(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    comments = Comment.objects.filter(post__id=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', post_pk=comment.post.pk)
    else:
        form = CommentForm()
    return render(request, 'my_blog/post_detail.html', {
        'post': post,
        'comments': comments,
        'form': form
    })


def post_list(request):
    posts = Post.objects.filter(deleted=False, draft=False)
    return render(request, 'my_blog/post_list.html', {'posts': posts})


def post_new(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'my_blog/post_edit.html', {'form': form})


def post_edit(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', post_pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'my_blog/post_edit.html', {'form': form})


def post_delete(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.deleted = True
    post.save()
    return redirect('post_draft_list')


def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True, deleted=False).order_by('-created_date')
    return render(request, 'my_blog/post_draft_list.html', {'posts': posts})


def post_publish(request, post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    post.publish()
    return redirect('post_detail', post_pk=post_pk)

def login(request):
    pass
