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
    
# import os
# import pdfkit
# from django.http import HttpResponse
# from django.template.loader import render_to_string
# from django.conf import settings

# def generate_pdf(request):
#     html_file = os.path.join(settings.BASE_DIR, 'templates', 'result.html')
#     html_string = render_to_string(html_file, {'name': 'John Doe', 'area': '42 sq. m', 'building': '70%'})
#     pdf = pdfkit.from_file(html_file, False, configuration=settings.PDFKIT_CONFIG)

#     response = HttpResponse(pdf, content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="result.pdf"'

#     return response

# from django.shortcuts import render
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa
# from io import BytesIO
# from . models import services

# def generate_pdf(request):
#     # Get the data you want to render
#     data = services.objects.all()

#     # Render the template with the data
#     template = get_template('result.html')
#     html = template.render({'data': data})

#     # Create a PDF file
#     response = HttpResponse(content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="services.pdf"'
#     buffer = BytesIO()
#     pdf = pisa.pisaDocument(BytesIO(html.encode("UTF-8")), buffer)
#     if not pdf.err:
#         response.write(buffer.getvalue())
#         buffer.close()
#         return response
#     else:
#         return HttpResponse('Error rendering PDF', status=400)

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
