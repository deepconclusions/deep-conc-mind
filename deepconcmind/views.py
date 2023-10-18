from django.shortcuts import render

def dashbord(request):
    template_name = 'dashbord.html'
    context = {}
    return render(request=request,
                  template_name=template_name,
                  context=context)

def howToDashbord(request):
    template_name = 'how_to_dashbord.html'
    context = {}
    return render(request=request,
                  template_name=template_name,
                  context=context)

def howToMindAi(request):
    template_name = 'how_to_mind_ai.html'
    context = {}
    return render(request=request,
                  template_name=template_name,
                  context=context)