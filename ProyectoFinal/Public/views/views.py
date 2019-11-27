from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django import forms
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView
from ..models import *

from django.views.generic import ListView

import sys
sys.path.append("..")
from Administracion.models import *
# Create your views here.

class addServicioForm(forms.ModelForm):
    class Meta:
        model = Servicios
        fields = ["nombre_servicio", "descripcion_servicio", "fecha_creacion_servicio", "fecha_modificacion_servicio", "status_servicio"]


class addServicio(CreateView):


    def get(self, request, *args, **kwargs):

           context = {'form': addServicioForm()}
           return render(request, 'Administracion/Base/Agregar/AdminAgregar.html', context)


    def post(self, request, *args, **kwargs):
        form = addServicioForm(request.POST)
        if form.is_valid():
            book = form.save()
            book.save()
            r = self.kwargs["un"]

            return HttpResponseRedirect(reverse_lazy('Public:calisBD' ))

