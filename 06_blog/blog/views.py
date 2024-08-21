from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.


def post_list(request):
    post = Post.objects.all()
    return render(request, 'home.html', {'post': post})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})