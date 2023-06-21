"""  este código realiza web scraping en la página web de Udemy para obtener 
informacion sobre el idioma y la calificación de los cursos, y guarda los resultados en un nuevo archivo CSV.
"""

import requests
import pandas as pd
from bs4 import BeautifulSoup


def scrap():
    """Realice un web scraping en la página web de udemy para extraer el lenguage y el rating."""
    df_udemy = pd.read_csv(r'C:\Users\cacer\OneDrive\Escritorio\PI02-MOOCs\Datasets\udemy_courses.csv')
    web_list = df_udemy['url'].to_list()

    #Creamos dos listas vacías para almacenar la información extraída
    rating_list = []
    language_list = []

    #Iteramos sobre cada URL en la lista web_list
    for webpage in web_list:
        #Realizamos una solicitud GET a la página web utilizando la biblioteca requests
        result = requests.get(webpage, timeout=2.50)
        #Obtenemos el contenido HTML de la página web
        content = result.text
        #Utilizamos BeautifulSouppara analizar el contenido HTML
        soup = BeautifulSoup(content, 'lxml')
        #Encuontramos el elemento HTML que contiene el idioma del curso:
        language = soup.find('div', class_='clp-lead__element-item clp-lead__locale')
        #Si no se encuentra el elemento del idioma, agregamos 'NoData'a la lista de lenguage
        if language is None:
            language_list.append('NoData')
        #De lo contrario, agregamos el texto de lenguage(obtenido usando get_text()) a la lista de lenguage después de eliminar los espacios en blanco
        else:
            language_list.append(language.get_text().strip())
        #Encontramos el elemento HTML que contiene la calificación del curso:    
        rating = soup.find('span', class_='ud-heading-sm star-rating-module--rating-number--2xeHu')
        #Si no se encuentra el elemento de rating, agregamos 'NoData'a la lista de rating
        if rating is None:
            rating_list.append('NoData')
        #De lo contrario, agregamos el texto de ratinga la lista de rating después de eliminar los espacios en blanco
        else:
            rating_list.append(rating.get_text().strip())
    #Agregamos las listas de lenguage y rating como nuevas columnas en el DataFrame df_udemy
    df_udemy['language'] = language_list
    df_udemy['rating'] = rating_list
    #Guardamos el DataFrame modificado en un nuevo archivo CSV:
    df_udemy.to_csv(r'C:\Users\cacer\OneDrive\Escritorio\PI02-MOOCs\Datasets\udemy.csv', index=False)

#Finalmente, llamamos a la función scrap() si el archivo se ejecuta directamente
if __name__ in '__main__':
    scrap()