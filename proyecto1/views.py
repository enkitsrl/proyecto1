from django.shortcuts import render_to_response
import datetime
import smtplib 
import requests
from bs4 import BeautifulSoup

def index(request):
    now = datetime.datetime.now()
    data = bank_Nacion()

    return render_to_response('index.html', {'current_date': now, 'data_nacion': data})

 
def bank_Nacion():
    informacion = []
    page_1 = requests.get('http://www.bna.com.ar/Personas')
    soup = BeautifulSoup(page_1.content, 'html.parser')
    contenedor = soup.find(id = 'billetes')

    tabla = contenedor.find(class_ = 'table cotizacion')
    rows = tabla.find_all('td')
    data = []
    i = 0
    for row in rows:
        i += 1
        if i == 3:
            data.append(row.get_text()) 
            i = 0
        else:
            data.append(row.get_text()) 
    data.append('Prueba')
    return data