from django.shortcuts import render
import json
import requests
import pandas as pd
# Create your views here.
api_key='4ac87f27590e5046eda6f7cedc638ce20124746b'
url_base= 'http://api.datosabiertos.presidencia.go.cr/api/v2/datastreams/'
guid= 'LICIT-ADJUD-DE-LAS-INSTI'
urlApi=url_base+guid+'/data.json/?auth_key='+api_key+'&limit=50'

def getData():
    response = requests.get(urlApi)
    if response.status_code == 200:
        data = json.loads(response.content)
        print(data)

getData()