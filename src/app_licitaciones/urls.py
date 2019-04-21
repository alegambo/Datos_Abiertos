from django.urls import path
from app_licitaciones.views import get_data_colones, get_data_dolar, load_index, get_all_data, load_information, \
    load_alldata_html
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', load_index, name='index'),
    path('licitaciones/', load_alldata_html, name='licitaciones'),
    path('allData/', get_all_data, name='allData'),
    path('DatosDolar/', get_data_dolar, name='dolars'),
    path('DatosColones/', get_data_colones, name='colones'),
    path('information/', load_information, name='information'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
