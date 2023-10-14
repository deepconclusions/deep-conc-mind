from django.db.models import Q
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import login
from django.contrib.auth import logout


def dashbord(request):
    template_name = 'dashbord.html'
    context = {}
    return render(request=request,
                  template_name=template_name,
                  context=context)