from django.shortcuts import render
from .models import Blog
import markdown

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    template_name = 'blog/blogs.html'
    return render(request=request,
                  template_name=template_name,
                  context= context)

def blogDetail(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    related_blogs = Blog.objects.filter(category=blog.category).order_by('-id')[:3]
    context = {
        'blog' : blog,
        'details': markdown.markdown(blog.body),
        'related_blogs' : related_blogs
        }
    template_name = 'blog/blog_detail.html'
    return render(request=request,
                  template_name=template_name,
                  context= context)