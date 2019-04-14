from django.http import HttpResponse
from django.shortcuts import render
import json
import requests
import pandas as pd
from pandas.io.json import json_normalize
# Create your views here.
api_key='4ac87f27590e5046eda6f7cedc638ce20124746b'
url_base= 'http://api.datosabiertos.presidencia.go.cr/api/v2/datastreams/'
guid= 'LICIT-ADJUD-DE-LAS-INSTI'
urlApi=url_base+guid+'/data.ajson/?auth_key='+api_key+'&limit=50&'

def getData(request):
    response = requests.get(urlApi)
    if response.status_code == 200:
        data = json.loads(response.content)
        nycphil = json_normalize(data,['result'])
        pe=pd.DataFrame(nycphil)
        soloDolar = pe[5] == 'USD'
        datawithDolar = pe[soloDolar]
        print(datawithDolar)

        return HttpResponse(datawithDolar.to_html())