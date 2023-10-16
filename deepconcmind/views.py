from django.shortcuts import render

def dashbord(request):
    template_name = 'dashbord.html'
    context = {}
    return render(request=request,
                  template_name=template_name,
                  context=context)