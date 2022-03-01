from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseNotFound
from password_manager_app.models import PasswordManager, Tag
from django.core.paginator import Paginator

def index(request):
    pass_list = PasswordManager.objects.order_by('-id')
    tags_list = Tag.objects.all()
    paginator = Paginator(pass_list, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
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
