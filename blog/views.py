from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .models import Post, Tag
from .utils import ObjectDetailMixin

def posts_list(request):
    posts = Post.objects.all()

    search = Post.objects.filter(slug__contains='new')
    context = {
        'posts':posts,
        'search':search,
    }
    return render(request, 'blog/index.html', context)

def tags_list(request):
    tags = Tag.objects.all()
    context = {
        'tags':tags,
    }
    return render(request, 'blog/tags_list.html', context)

class PostDetail(ObjectDetailMixin, View):
    model = Post
    template = 'blog/post_detail.html'

class TagDetail(ObjectDetailMixin, View):
    model = Tag
    template = 'blog/tag_detail.html'
