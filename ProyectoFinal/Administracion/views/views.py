from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.views.generic import CreateView
from django import forms
from ..models import *
# Create your views here.

class formvistaTemplate(forms.ModelForm):
    class Meta:
        model = Libro

        fields = ['titulo_libro', 'no_paginas_libro', 'fecha_creacion_libro', 'fecha_modificacion_libro', 'autor',
                  'categoria', 'editorial', 'sucursal', 'sinopsis', 'status_libro', 'vistas', 'costo']
        widgets = {
            'sucursal': forms.CheckboxSelectMultiple(),
            'sinopsis': forms.Textarea()
        }


    def __init__(self, *args, **kwargs):
        super(formvistaTemplate, self).__init__(*args, **kwargs)
        self.fields['categoria'].queryset = Categoria.objects.filter(status_categoria='A')
        self.fields['autor'].queryset = Autor.objects.filter(status_autor='A')
        self.fields['editorial'].queryset = Editorial.objects.filter(status_editorial='A')
        self.fields['sucursal'].queryset = Sucursales.objects.filter(status_sucursal='A')

class vistaTemplate(CreateView):
    def get(self, request, *args, **kwargs):
        context = {'form':formvistaTemplate()}
        return render(request, 'Administracion/Base/Agregar/AdminAgregar.html', context)

    def post(self, request, *args, **kwargs):
        form = formvistaTemplate(request.POST)

        if form.is_valid():
            Libro = form.save()
            Libro.save()
            return HttpResponseRedirect(reverse_lazy('Administracion:vistaTemplate'))
        return render(request, 'Administracion/Base/Agregar/AdminAgregar.html', {'form':form})