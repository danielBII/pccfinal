
from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from blog.forms import PostForm
import re
import unidecode
from django.contrib.auth.decorators import login_required


def home(request):
    posts = Post.objects.all()

    context = {
        'posts': posts
    }
    return render(request, 'Home/index.html', context)

@login_required
def posts_edit(request, slug):
    post = get_object_or_404(Post, pk=slug)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'CrudPost/create.html', context)



def posts(request, slug):
    

    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post
    }
    return render(request, 'Blog/index.html', context)

@login_required
def posts_create(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            
            title_slug = unidecode.unidecode(request.POST['title']).lower()
            slug = re.sub(r'[\W_]+', '-', title_slug)

            post = form.save(commit=False)
            post.author = request.user
            post.slug = slug
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
        else:
            return render(request, 'CrudPost/create.html', {'form': form})
    else:
        form = PostForm()
    return render(request, 'CrudPost/create.html', {'form': form})


@login_required
def posts_del(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        post.delete()        
        return redirect('/')
    else:
        form = PostForm(instance=post)
    context = {
        'form':form
    }
    return render(request, 'CrudPost/delete.html', context)

def view_desenv(request):
    return render(request, 'dev.html')