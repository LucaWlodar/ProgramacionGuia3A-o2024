import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def descargar_imagenes(https://www.clarin.com/tema/arte.html, descargas):
    if not os.path.exists(carpeta_destino):
        os.makedirs(carpeta_destino)
    response = requests.get(url_pagina)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    imagenes = soup.find_all('img')
    
    for img in imagenes:
        img_url = urljoin(url_pagina, img['src'])
        
        nombre_archivo = os.path.basename(img_url)
        
        with open(os.path.join(carpeta_destino, nombre_archivo), 'wb') as f:
            imagen_respuesta = requests.get(img_url)
            f.write(imagen_respuesta.content)
            print(f"Imagen descargada: {nombre_archivo}")

url_pagina = "https://www.clarin.com/tema/arte.html"

carpeta_destino = "imagenes_descargadas"

descargar_imagenes(url_pagina, desca)
