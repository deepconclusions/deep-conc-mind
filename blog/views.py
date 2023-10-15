from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(request):
    blogs = Blog.objects.all()
    context = {'blogs' : blogs}
    template_name = 'blog/blogs.html'
    return render(request=request, 
                  template_name=template_name, 
                  context= context)