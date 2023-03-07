from django.shortcuts import render
from django.http import HttpResponse
from .forms import serviceform
# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def service(request):
    form = serviceform()
    dict_form = {
        'form': form
    }
    return render(request,'service.html', dict_form)

def result(request):
    if request.method == 'POST':
        # process form data here
        name = request.POST.get('Name')
        area = request.POST.get('area_of_site')
        choice = request.POST.get('Your_dream_building')

        # render results page with context
        context = {
            'name': name,
            'area': area,
            'building': choice
        }
        return render(request, 'result.html', context)