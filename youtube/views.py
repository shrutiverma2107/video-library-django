from django.shortcuts import render
from youtube.models import Videos
from django.http import HttpResponse
from django.views.generic import ListView

def index(request):
    template_name = 'video.html'
    vd = Videos.objects.all()
    if request.GET.get('search'):
        query = request.GET.get('search')
        vd = Videos.objects.filter(name__icontains=query)
    else :
        vd=Videos.objects.all() # Collect all records from table 
    return render(request,'video_library_single.html',{'videos':vd})
