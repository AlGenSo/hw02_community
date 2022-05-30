from django.shortcuts import get_object_or_404, render
from .models import Post, Group


# view-функция для главной страницы
def index(request):
    template = 'posts/index.html'
    posts = Post.objects.order_by('-pub_date')[:10]
    title = 'Последние обновления на сайте'
    h1text = 'Последние обновления на сайте'
    context = {
        'title': title,
        'posts': posts,
        'h1text': h1text,
    }

    return render(request, template, context)


# view-функция для страницы на которой будут посты
def groups_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by('-pub_date')[:10]
    title = 'Записи сообщества Лев Толстой – зеркало русской революции.'
    h1text = 'Лев Толстой – зеркало русской революции.'
    ptext = 'Группа тайных поклонников графа.'
    context = {
        'title': title,
        'group': group,
        'posts': posts,
        'h1text': h1text,
        'ptext': ptext,
    }

    return render(request, template, context)
