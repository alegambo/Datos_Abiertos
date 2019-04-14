from django.urls import path
from app_licitaciones.views import getData
urlpatterns = [
    path('prueba/', getData),

]