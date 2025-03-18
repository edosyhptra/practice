from django.urls import path
from .views import read, create, list, delete, notfound, update

urlpatterns = [
    path('create/', create.view, name='blog-create'),
    path('<int:id>/', read.view, name='blog-read'),
    path('list/', list.view, name='blog-list'),
    path('delete/<int:id>/', delete.view, name='blog-delete'),
    path('not-found/', notfound.view, name='blog-notfound'),
    path('update/<int:id>/', update.view, name='blog-update'),
]