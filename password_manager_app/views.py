from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseNotFound
from password_manager_app.models import PasswordManager, Tag
from django.core.paginator import Paginator
from django.db.models import Q
from .forms import PasswordManagerForm
from django.contrib.auth.decorators import login_required
from django.http import Http404


kirill = ('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
kirill = kirill + kirill.upper()

@login_required
def index(request):
    search_query = request.GET.get('q', '')
    for letter in search_query:
        if letter in kirill:
            search_query = search_query.lower()
            break
    if search_query:
        pass_list = PasswordManager.objects.filter(
            (Q(ip__icontains=search_query) |
            Q(login__icontains=search_query) |
            Q(resource_name_alias__icontains=search_query)) &
            Q(post_author=request.user)
        )
    else:
        pass_list = PasswordManager.objects.filter(post_author=request.user).order_by('-id')
    tags_list = Tag.objects.order_by('name')
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list
    }
    return render(request, 'password_manager_app/manager.html', context=context)


@login_required
def get_tag(request, tag):
    tagname = get_object_or_404(Tag, slug=tag)
    pass_list = PasswordManager.objects.filter(post_author=request.user).order_by('-id')
    tags_list = Tag.objects.order_by('name')
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list,
        'tagname': tagname,
    }
    return render(request, 'password_manager_app/selected.html', context=context)


@login_required
def new_post(request):
    """Определяет новую тему."""
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PasswordManagerForm()
    else:
        # Отправлены данные POST; обработать данные.
        userid = request.user
        form = PasswordManagerForm(data=request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post_author = userid
            form.save()
        return redirect('index')
    context = {
        'form': form,
    }
    return render(request, 'password_manager_app/new_post.html', context)


@login_required
def edit_post(request, post_slug):
    """Редактирует существующую запись."""
    post = get_object_or_404(PasswordManager, post_slug=post_slug)
    name = post.post_author
    if post.post_author != request.user:
        raise Http404
    if request.method != 'POST':
        # Данные не отправлялись; создается пустая форма.
        form = PasswordManagerForm(instance=post)
    else:
        # Отправлены данные POST; обработать данные.
        form = PasswordManagerForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
        return redirect('index')
    return render(request, 'password_manager_app/post_page.html', context={'post': post, 'form':form})


@login_required
def delete_post(request, post_slug):
    post = get_object_or_404(PasswordManager, post_slug=post_slug)
    if request.method != 'POST':
        form = PasswordManagerForm(instance=post)
    else:
        form = PasswordManagerForm(instance=post, data=request.POST)
        post.delete()
        # return redirect('index')
        return render(request, 'password_manager_app/del_post.html', context={'post': post, 'form': form})
    # return render(request, 'password_manager_app/del_post.html', context={'post': post, 'form':form})
    return redirect('index')