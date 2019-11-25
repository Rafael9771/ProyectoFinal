from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class vistaTemplate(TemplateView):
    template_name = 'Administracion/Base/Agregar/AdminAgregar.html'
