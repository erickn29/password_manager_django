from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('<str:tag>', views.get_tag, name='tags'),
]
