from django.urls import path

from .views.views import *

app_name = "Administracion"

urlpatterns = [
    path('', vistaTemplate.as_view(), name="vistaTemplate"),
    path('inicio', inicio.as_view(), name="inicio"),
    path('adminP', metodo, name="metodo"),
    path('adminP/addAdmin', addUsuarioAdmin.as_view(), name="inicioAdminP"),

    #validaciones ajax
    path('validacionAdmin', validate_Admin, name="validarAdmin"),
    path('AdminExist', admin_exist, name="AdminExist"),
]