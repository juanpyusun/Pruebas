

"""

Código para hacer el scraping de la página Punto propiedad. En este código el web scraping se realiza usando Beautiful soup. 

Los parametros que se requieres son: tipo de inmueble('locales-comerciales','oficinas','bodegas', 'edificios') , ciudad ('Bogota', 'Cali', 'Barranquilla' o 'Medellin') y tipo de transacción ('arriendo' o 'venta'). 

El output es un archivo json con la información 

"""

# se importan las librerias necesarias 

from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from parsel import Selector

import requests

from bs4 import BeautifulSoup

import math

from collections import defaultdict

import pandas as pd

import json

import unicodedata

import re

from time import sleep

from tqdm import tqdm

import sys

import argparse





#Funciones utiles para la edicion de los datos

def normalize(c):

    return unicodedata.normalize("NFD",c)[0]



def to_int(palabra):

    return  int(''.join(re.findall('\d+', palabra )))



#Parametros necedarios: tipo de inmueble, ciudad, tipo de transacción, ciudad

#NOTA: En ocasiones es necesario dividir la lista porque se puede caer la conexión si se tarda mucho la obtención de datos

inmuebles = [ 'locales-comerciales','oficinas','bodegas', 'edificios']

# ciudades = ['bogota','barranquilla','medellin','cali']

# tipo_transaccion = 'arriendo'

# ciudad = "medellin"



print('Incia corrida: ')

def PuntoPropiedad(ciudad,tipo_transaccion):      

    for inmueble in tqdm(inmuebles):

        print('Tipo de inmueble: ' + inmueble)

        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36'}

        #Url inicial: Se ponen filtros: tipo de transaccion, tipo de inmueble y la ciudad 

        url_request = "https://www.puntopropiedad.com/"+tipo_transaccion+"/"+inmueble+"/"+ciudad

        # specifies the path to the chromedriver.exe

        driver = webdriver.Chrome(r'C:\Users\Usuario\Downloads\chromedriver_win32 (2)/chromedriver.exe')

        # driver.get method() will navigate to a page given by the URL address

        driver.get(url_request)

        source = driver.page_source

        data_request = BeautifulSoup(source,"html.parser")

        



        #Se obtiene el total de items encontrados para saber el total de paginas

        print(data_request)

        data_total = data_request.findAll('h1',attrs={'class':'titular'})

        print('DATAAAAAAAAAAAAAAAAAAAAAAAAAaaa')

        print(data_total)        

        try:

            total_items = int((data_total[0].text.split()[0]))

        except: 

            total_items = to_int((data_total[0].text.split()[0]))

        total_items = (math.ceil(total_items/15))



        #Primera pagina

        data_inmueble = data_request.findAll('h2',attrs={'class':'title'})

        #Se inicializa una lista para guardar los links que aparezcan en el pagina principal de busqueda

        lista_links = []

        #Se recorre los links obtenidos para irlos guardando

        print('Obtaining links:')

        for div in data_inmueble:

            links = div.findAll('a')

            for a in links:

                lista_links.append('https://www.puntopropiedad.com'+a['href'])

                



        print("Obtaining links: ")

        for i in tqdm(range(2,total_items+1)):



            url_request = "https://www.puntopropiedad.com/"+tipo_transaccion+"/"+inmueble+"/"+ciudad+"/p_"+str(i)

            # driver.get method() will navigate to a page given by the URL address

            driver.get(url_request)

            source = driver.page_source

            data_request = BeautifulSoup(source,"html.parser")



            #Se obtiene la data de donde podemos extraer todos los links asociados a un inmueble

            data_inmueble = data_request.findAll('h2',attrs={'class':'title'})

            #Se inicializa una lista para guardar los links que aparezcan en el pagina principal de busqueda

            #Se recorre los links obtenidos para irlos guardando

            for div in data_inmueble:

                links = div.findAll('a')

                for a in links:

                    lista_links.append('https://www.puntopropiedad.com'+a['href'])



        diccionario = dict()

        item = 0



        print('Obtaining all data:')

        for j in tqdm(lista_links):

            url = j

            item = item +1

            # driver.get method() will navigate to a page given by the URL address

            driver.get(url)

            source = driver.page_source

            data = BeautifulSoup(source,"html.parser")

            try:

            # Se encuentran los elementos de inte´res que se quieren extraer de la página web, con base en la clase. 

                nombre = data.find("h2", {"class": "detail-subtitle"}).text 

                print(nombre)

            except:

                nombre = " "

            try:

                description = data.find("p", {"class": "description long_text"}).text

                description = ''.join(normalize(c) for c in str(description))

                print(description)

            except:

                description = 'No hay'

            try:    

                other_element = data.find_all("li", {"class": "tick"})

            except:

                other_element = ' No elementos'

            try: 

                price = data.find("p", {"class": "price"}).text

                price = int(''.join(re.findall('\d+', price )))

            except:

                price = price

            data_agente = data.findAll('h2',attrs={'class':'title'})

            #Obtener link de quien publicó

            for div in data_agente:

                links = div.findAll('a')

                for a in links:

                    publicador =('https://www.puntopropiedad.com'+a['href'])



            #Se guardan los elementos de interés en el diccionario

            text = (other_element)

            lista_elementos = []

            diccionario[item] ={}

            diccionario[item]['Nombre'] =  nombre

            diccionario[item]['publicador'] =  publicador

            diccionario[item]['descripcion'] =  description

            diccionario[item]['url'] =  j

            diccionario[item]['price'] =  price

            diccionario[item]['tipo inmueble'] =  inmueble

            diccionario[item]['Ciudad'] = ciudad

            diccionario[item]['Tipo transaccion'] = tipo_transaccion

            if len(text) != 0:

                for i in range(0, len(text)):

                    lista_elementos.append(text[i].text)

                    diccionario[item]['elementos'] = lista_elementos

            (diccionario.update(diccionario))

        #Se guarda el json 

        name = ciudad+"_"+tipo_transaccion+"_"+inmueble+".json"

        with open(name, 'w') as file:

            json.dump(diccionario, file, indent=4)







parser = argparse.ArgumentParser(description='Código para hacer web scraping de la fuente Punto Propiedad')

parser.add_argument('-ciudad','--ciudad', help='''Coloque alguna de las opciones: 'bogota','barranquilla','medellin','cali''', required=True)

parser.add_argument('-transaccion','--transaccion', help='''Coloque alguna de las opciones: 'arriendo' o 'venta''', required=True)



if __name__ == "__main__":

   PuntoPropiedad(sys.argv[1], sys.argv[2])

