from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.utils import timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User



def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {'post': post})

# @login_required
def post_new(request):
    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('post_list')

# @login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        if request.method == "POST":
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user
                # post.published_date = timezone.now()
                post.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm(instance=post)
        return render(request, 'blog/post_edit.html', {'form': form})
    else:
        return redirect('post_detail', pk=post.pk)

# @login_required
def post_draft_list(request):
    if request.user.is_superuser:
        posts = Post.objects.filter(published_date__isnull=True).order_by('-created_date')
        return render(request, 'blog/post_draft_list.html', {'posts': posts})
    else:
        return redirect('post_list')

# @login_required
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_superuser:
        post.publish()
        return redirect('post_detail', pk=pk)
    else:
        return redirect('post_detail', pk=pk)


# @login_required
def post_delete(request, pk):
    if request.user.is_superuser:
        post = get_object_or_404(Post, pk=pk)
        post.delete()
        return redirect('post_list')
    else:
        return redirect('post_list')


def post_logout(request):
    logout(request)
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated():
        name = request.user.username
        form = CommentForm(initial={'author': name})
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.approve()
                comment.save()
                return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.post = post
                comment.save()
                return redirect('post_detail', pk=post.pk)
    # else:
            # form = CommentForm()
    return render(request, 'blog/add_comment_to_post.html', {'form': form})

# @login_required
def comment_approve(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_superuser:
        comment.approve()
        return redirect('post_detail', pk=comment.post.pk)
    else:
        return redirect('post_detail', pk=comment.post.pk)

# @login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.user.is_superuser:
        post_pk = comment.post.pk
        comment.delete()
        return redirect('post_detail', pk=post_pk)
    else:
        return redirect('post_detail', pk=comment.post.pk)















