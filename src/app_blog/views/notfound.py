from django.shortcuts import render

def view(request):
    return render(request, 'app_blog/not_found.html', name='blog-notfound')