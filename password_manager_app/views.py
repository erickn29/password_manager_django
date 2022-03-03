from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from password_manager_app.models import PasswordManager, Tag
from django.core.paginator import Paginator
from django.db.models import Q
from itertools import chain


def index(request):
    search_query = request.GET.get('q', '')
    if search_query:
        pass_list = PasswordManager.objects.filter(
            Q(ip__icontains=search_query) |
            Q(login__icontains=search_query.lower()) |
            Q(tags__name__icontains=search_query.lower())
        )
    else:
        pass_list = PasswordManager.objects.order_by('-id')
    tags_list = Tag.objects.all()
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list
    }
    return render(request, 'password_manager_app/manager.html', context=context)


def get_tag(request, tag):
    tagname = get_object_or_404(Tag, slug=tag)
    pass_list = PasswordManager.objects.all()
    tags_list = Tag.objects.all()
    paginator = Paginator(pass_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'pass_list': pass_list,
        'tags_list': tags_list,
        'tagname': tagname,
    }
    return render(request, 'password_manager_app/selected.html', context=context)


# def get_search_result(request):
#     search_query = request.GET.get('q', '')
#     if search_query:
#         pass_list = PasswordManager.objects.filter(
#             Q(ip__icontains=search_query) |
#             Q(login__icontains=search_query.lower()) |
#             Q(tags__name__icontains=search_query.lower())
#         )
#     else:
#         pass_list = PasswordManager.objects.order_by('-id')
#     tags_list = Tag.objects.all()
#     return render(request, 'password_manager_app/search.html', context={
#         'pass_list': pass_list,
#         'tags_list': tags_list,
#     })

# def index(request):
#     pass_list = PasswordManager.objects.order_by('-id')
#     tags_list = Tag.objects.all()
#     paginator = Paginator(pass_list, 10)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {
#         'pass_list': pass_list,
#         'tags_list': tags_list
#     }
#     return render(request, 'password_manager_app/manager.html', context=context)

