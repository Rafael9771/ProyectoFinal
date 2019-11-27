from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.template.loader import get_template
from django.views.generic import CreateView, TemplateView
from django import forms
from ..models import *

def validate_Admin(request):
    username = request.GET.get('username', None)
    password = request.GET.get('password', None)
    if username == 'AdminP' and password == 'Omeghax9771':
        data = {'is_default': 'Inicio con el admin de defecto en la pag'}
    else:
        data = {
            'is_taken': Usuario.objects.filter(username=username, password=password).exists()
        }
        if data['is_taken']:
            data['error_message'] = 'A user with this username already exists.'
    return JsonResponse(data)

def admin_exist(request):
    username = request.GET.get('username', None)

    data = {
        'is_taken': Usuario.objects.filter(username=username).exists()
    }
    if data['is_taken']:
        data['error_message'] = 'A user with this username already exists.'

    return JsonResponse(data)

def metodo(request):
    context = {
    }

    if request.method == 'POST':
        return HttpResponseRedirect(reverse_lazy('Administracion:inicioAdminP'))
    else:
        print("No entro al post")

        return HttpResponseRedirect(reverse_lazy('Administracion:inicio'))

class inicio(TemplateView):
    template_name = 'Administracion/Base/InicioSesion/inicio.html'


class addUsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['username', 'password', 'fecha_creacion', 'fecha_modificacion', 'status']
        widgets = {
            'password': forms.PasswordInput()
        }



class addUsuarioAdmin(CreateView):


    def get(self, request, *args, **kwargs):

        context = {'form': addUsuarioForm}
        return render(request, 'Administracion/Base/AdminP/InicioAdminP.html', context)


    def post(self, request, *args, **kwargs):
        form = addUsuarioForm(request.POST)
        nombre = request.POST['username']

        if form.is_valid():
            book = form.save()
            book.save()

            return HttpResponseRedirect(reverse_lazy('Administracion:inicioAdminP'))



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