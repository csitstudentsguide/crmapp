from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    all_posts = Post.newmanager.all()
    context = {'posts': all_posts}
    return render(request, 'blog/index.html', context=context)

def single_post_view(request, post):    
    single_post = Post.objects.get(slug=post)
    all_posts = Post.newmanager.all()
    context = {'post': single_post, 'posts': all_posts}
    return render(request, 'blog/single-post-view.html', context=context)

