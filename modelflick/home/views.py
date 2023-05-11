from django.shortcuts import render
from django.http import HttpResponse
from .forms import serviceform




# Create your views here.
def pointer(request):
    return render(request,'pointer.html')

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def service(request):
    form = serviceform()
    dict_form = {
        'form': form
    }
    return render(request,'service.html', dict_form)

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.http import HttpResponse
from .models import services

def generate_pdf(request):
    # Get the data from the model
    data = services.objects.all()

    print(data)


    # Create a PDF file
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="services.pdf"'
    pdf = canvas.Canvas(response, pagesize=letter)

    # Set text formatting
    pdf.setFillColorRGB(0, 0, 0.8)
    pdf.setFont("Helvetica", 12)

    # Add the data to the PDF
    textobject = pdf.beginText()
    textobject.setTextOrigin(50, 750)
    for obj in data:
        textobject.textLine("Name: {}".format(obj.Name))
        textobject.textLine("Area of Site: {}".format(obj.area_of_site))
        textobject.textLine("Your Dream Building: {}".format(obj.Your_dream_building))
        textobject.textLine("")
    pdf.drawText(textobject)

    # Close the PDF
    pdf.showPage()
    pdf.save()
    return response

from django.shortcuts import render, redirect
from .forms import serviceform
from .models import services

def my_view(request):
    if request.method == 'POST':
        form = serviceform(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()
            return render(request, 'result.html')
    form = serviceform()
    dict_form={
        'form': form
    }
    return render(request, 'service.html',dict_form)

from django.shortcuts import render
from .models import services

def result(request):
    servicess= services.objects.all()
    return render(request,'result.html', {'servicess': servicess})