from django.urls import path
from .views import read, create, list

urlpatterns = [
    path('', create.view, name='blog-create'),
    path('<int:id>/', read.view, name='blog-read'),
    path('list/', list.view, name='blog-list'),
]