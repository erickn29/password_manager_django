from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from password_manager_app.models import PasswordManager, Tag
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PasswordManagerForm


def index(request):
    search_query = request.GET.get('q', '')
    if search_query:
        pass_list = PasswordManager.objects.filter(
            Q(ip__icontains=search_query) |
            Q(login__icontains=search_query)
            # Q(tags__name__icontains=search_query)
        )
    else:
        pass_list = PasswordManager.objects.order_by('-id')
    tags_list = Tag.objects.order_by('name')
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list
    }
    return render(request, 'password_manager_app/manager.html', context=context)


def get_tag(request, tag):
    tagname = get_object_or_404(Tag, slug=tag)
    pass_list = PasswordManager.objects.order_by('-id')
    tags_list = Tag.objects.order_by('name')
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list,
        'tagname': tagname,
    }
    return render(request, 'password_manager_app/selected.html', context=context)


def new_post(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PasswordManagerForm()
    else:
        # Отправлены данные POST; обработать данные.
        form = PasswordManagerForm(data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'password_manager_app/new_post.html', context)





