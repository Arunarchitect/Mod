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
    
import os
import pdfkit
from django.http import HttpResponse
from django.template.loader import render_to_string
from django.conf import settings

def generate_pdf(request):
    html_file = os.path.join(settings.BASE_DIR, 'templates', 'result.html')
    html_string = render_to_string(html_file, {'name': 'John Doe', 'area': '42 sq. m', 'building': '70%'})
    pdf = pdfkit.from_file(html_file, False, configuration=settings.PDFKIT_CONFIG)

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="result.pdf"'

    return response

