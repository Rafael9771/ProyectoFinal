from django.urls import path
from .views.views import *


app_name = "Public"

urlpatterns = [
    path('addLogin', addServicio.as_view(), name="calisBD"),

]