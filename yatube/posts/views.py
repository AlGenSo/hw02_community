from django.shortcuts import get_object_or_404, render

from .models import Post, Group
from .constants import LIMIT_COUNTS_POSTS


def index(request):
    '''view-функция для главной страницы'''
    template = 'posts/index.html'
    posts = Post.objects.select_related('author', 'group')[:LIMIT_COUNTS_POSTS]
    context = {
        'posts': posts,
    }

    return render(request, template, context)


def groups_posts(request, slug):
    '''view-функция для страницы на которой будут посты'''
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group)[:LIMIT_COUNTS_POSTS]
    context = {
        'group': group,
        'posts': posts,
    }

    return render(request, template, context)
