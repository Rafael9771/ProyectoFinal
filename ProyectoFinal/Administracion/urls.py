from django.urls import path

from .views.views import *

app_name = "Administracion"

urlpatterns = [
    path('', vistaTemplate.as_view(), name="vistaTemplate"),
]