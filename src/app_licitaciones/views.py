from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
import io

# Create your views here.
api_key = '4ac87f27590e5046eda6f7cedc638ce20124746b'
url_base = 'http://api.datosabiertos.presidencia.go.cr/api/v2/datastreams/'
guid = 'LICIT-ADJUD-DE-LAS-INSTI'
urlApi = url_base + guid + '/data.ajson/?auth_key=' + api_key + '&limit=50&'
response = requests.get(urlApi)
pd.set_option('max_colwidth', 100)

def load_index(request):
    """
    This function render the index.html, this is the main page
    :param request:
    :return: Render index.html
    """
    return render(request, 'index.html')


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
        data = getAll_data()
        datoshtml = data['htmlT']

        return HttpResponse(datoshtml)


def getAll_data():
    dataF = {}
    if response.status_code == 200:
        data = json.loads(response.content)
        nycphil = json_normalize(data, ['result'])
        allData = pd.DataFrame(nycphil)
        allData.columns = ['Año', 'Institución', 'Tipo Trámite', 'Proveedor Adjudicado', 'Fecha de Adjudicación',
                           'Moneda', 'Monto Adjudicado']
        allData.drop(allData.index[[0]], inplace=True)
        allData['Año'] = pd.to_numeric(allData['Año'], errors='coerce')
        buf = io.StringIO()
        allData.info(buf=buf)
        show_info = buf.getvalue()
        dataF['Info'] = show_info
        dataF['Dimensiones'] = allData.shape
        dataF['Columnas'] = allData.columns.values
        dataF['htmlT'] = allData.to_html()
        allData
        return dataF


def load_alldata_html(request):
    alldataLic = getAll_data()
    dim = alldataLic['Dimensiones']
    info = alldataLic['Info']
    columnas = alldataLic['Columnas']
    htmlT = alldataLic['htmlT']
    context = {
        'columnas': columnas,
        'info': info,
        'dimensiones': dim,
        'tablahtmlT': htmlT,
    }
    return render(request, 'observLicitaciones.html', context)


def load_information(request):
    """
    This function render the information.html
    :param request:
    :return: Render information.html
    """
    return render(request, 'information.html')
