from django.shortcuts import render, redirect
from .models import Galery
from .forms import GaleryForm
from django.utils import timezone


def galery(request):
    galery = Galery.objects.all()
    context = {
        'galery': galery
    }
    return render(request, 'galery.html', context)


def create_post_galery(request):
    if request.method == "POST":
        form = GaleryForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('/')
        else:
            return render(request, 'form_galery.html', {'form': form})
    else:
        form = GaleryForm()
    return render(request, 'form_galery.html', {'form': form})
