from django.urls import path
from app_licitaciones.views import get_data_colones, get_data_dolar, load_index, get_all_data

urlpatterns = [
    path('', load_index, name='index'),
    path('allData/', get_all_data, name='allData'),
    path('DatosDolar/', get_data_dolar, name='dolars'),
    path('DatosColones/', get_data_colones, name='colones'),

]
