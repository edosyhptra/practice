from django.shortcuts import redirect
from app_blog.utility import query

def view(request, id):
    if request.method == 'GET':
        post = query('DELETE FROM blog_post WHERE id =%s', [id])
        print(post)
    
    return redirect("/blog/list", name='blog-delete')