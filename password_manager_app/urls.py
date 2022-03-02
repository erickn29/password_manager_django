from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('search', views.get_search_result, name='search_results'),
    path('<str:tag>', views.get_tag, name='tags'),
]
