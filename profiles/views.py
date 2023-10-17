from django.shortcuts import render
from .models import Profile

# Create your views here.
def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    template_name = 'profiles/profiles.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)

def profileDetail(request, profile_id):
    profile = Profile.objects.get(id=profile_id)
    context = {'profile': profile}
    template_name = 'profiles/profile.html'
    return render(request=request, 
                  template_name=template_name, 
                  context=context)
