from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize

# Create your views here.
api_key = '4ac87f27590e5046eda6f7cedc638ce20124746b'
url_base = 'http://api.datosabiertos.presidencia.go.cr/api/v2/datastreams/'
guid = 'LICIT-ADJUD-DE-LAS-INSTI'
urlApi = url_base + guid + '/data.ajson/?auth_key=' + api_key + '&limit=50&'
response = requests.get(urlApi)


def get_data_dolar(request):
    if response.status_code == 200:
        data = json.loads(response.content)
        nycphil = json_normalize(data, ['result'])
        frame = pd.DataFrame(nycphil)
        frame.columns = ['Año', 'Institución', 'Tipo Trámite', 'Proveedor Adjudicado', 'Fecha de Adjudicación',
                         'Moneda', 'Monto Adjudicado']
        justDolar = frame['Moneda'] == 'USD'
        datawithDolar = frame[justDolar]

        return HttpResponse(datawithDolar.to_html())


def get_data_colones(request):
    if response.status_code == 200:
        data = json.loads(response.content)
        nycphil = json_normalize(data, ['result'])
        frame = pd.DataFrame(nycphil)
        frame.columns = ['Año', 'Institución', 'Tipo Trámite', 'Proveedor Adjudicado', 'Fecha de Adjudicación',
                         'Moneda', 'Monto Adjudicado']
        justColones = frame['Moneda'] == 'CRC'
        datawithDolar = frame[justColones]

        return HttpResponse(datawithDolar.to_html())


def get_all_data(request):
    if response.status_code == 200:
        data = json.loads(response.content)
        nycphil = json_normalize(data, ['result'])
        allData = pd.DataFrame(nycphil)

        return HttpResponse(allData.to_html())


def load_index(request):
    """
    This function render the index.html, this is the main page
    :param request:
    :return: Render index.html
    """
    return render(request, 'index.html')
