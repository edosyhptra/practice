from django.urls import path
from .views import read, create

urlpatterns = [
    path('', create.view, name='blog-create'),
    path('<int:id>/', read.view, name='blog-read'),
]