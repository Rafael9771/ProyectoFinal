from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from ..models import *
from django.views.generic import ListView
# Create your views here.

class i(ListView):

    def get(self, request, *args, **kwargs):
        m = favoritos.objects.all()
        context = {
            'fav':m
        }
        template = get_template('Administracion/Base/Agregar/AdminAgregar.html')
        html = template.render(context)
        return HttpResponse(html)