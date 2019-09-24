#!/usr/bin/python
import smtplib 
import requests
from bs4 import BeautifulSoup

def bank_Nacion():
    informacion = []
    page_1 = requests.get('http://www.bna.com.ar/Personas')
    soup = BeautifulSoup(page_1.content, 'html.parser')
    contenedor = soup.find(id = 'billetes')

    tabla = contenedor.find(class_ = 'table cotizacion')
    rows = tabla.find_all('td')
    data = 'Banco Nacion ' + '\n' + '--------------' + '\n'
    i = 0
    for row in rows:
        i += 1
        if i == 3:
            data = data +' '+(row.get_text()) + '\n' + '--------------' + '\n'
            i = 0
        else:
            data = data +' '+(row.get_text()) + '\n'
            
    return data
def  bank_santander():
    page_1 = requests.get('https://banco.santanderrio.com.ar/exec/cotizacion/index.jsp')
    soup = BeautifulSoup(page_1.content, 'html.parser')
    rows = soup.find_all('td')
    data = 'Banco Santander Rio ' + '\n' + '------------------' + '\n'
    i = 0
    for row in rows:
        i += 1
        if i == 3:
            data = data +' '+(row.get_text()) + '\n' + '------------------' + '\n'
            i = 0
        else:
            data = data +' '+(row.get_text()) + '\n'
    
    return(data)

def send_email(mensaje , destino):
    emisor = 'lucasezequielgo@gmail.com'
    asunto = 'Cotizacion del dia'
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    try:
        server.login(emisor ,'Eqlocer7')
        server.sendmail(emisor, destino ,mensaje.encode('utf-8').strip())
        server.quit()
        print('Correo enviado con exito')
    except:
        print('Error al enviar el E-mail')
    

