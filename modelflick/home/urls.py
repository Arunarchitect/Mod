from django.urls import path , include
from . import views
from .views import generate_pdf, serviceview
urlpatterns = [
    path('', views.index, name='home'),
    path('about', views.about, name='about'),
    path('service', views.my_view, name='service'),
    path('service/result/', serviceview.as_view, name='result'),
    path('generate-pdf/', generate_pdf, name='generate-pdf'),
]