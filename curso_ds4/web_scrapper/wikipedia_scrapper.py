import os
import requests
from bs4 import BeautifulSoup
import argparse
import json

def scrap(url: str):
    print(f"[+] Descargando: {url}")
    pagina = requests.get(url, timeout=10)
    if pagina.status_code != 200:
        raise Exception(f'[!] Error {pagina.status_code} en la página {url}')
    return pagina

def guardar_pagina(pagina, nombre_archivo: str):
    with open(nombre_archivo, "wb") as f:
        f.write(pagina.content)
    print(f'[+] Página guardada en {nombre_archivo}')

def main(url: str, archivo_salida: str):
    if not os.path.exists(archivo_salida):
        pagina = scrap(url)
        guardar_pagina(pagina, archivo_salida)
        contenido = pagina.content
    else:
        print(f'[i] El archivo {archivo_salida} ya existe. Leyendo de él.')
        with open(archivo_salida, 'rb') as f:
            contenido = f.read()

    soup = BeautifulSoup(contenido, "html.parser")

    # Intentamos con 'mw-pages' primero
    main_content = soup.find('div', id='mw-pages')
    if not main_content:
        # Si no funciona, probamos con 'mw-content-text' o 'mw-body-content'
        print('[!] No se encontró <div id="mw-pages">, probando con "mw-content-text"...')
        main_content = soup.find('div', id='mw-content-text')

    if not main_content:
        print('[x] No se encontró ningún contenedor útil. Abortando.')
        return

    lis = main_content.find_all('li')
    print(f'[+] Encontrados {len(lis)} elementos <li>')

    if not lis:
        print('[x] No hay elementos <li>. No se genera el JSON.')
        return

    diccionario_lis = {}
    for li in lis:
        if li.a:
            texto = li.a.text.strip()
            href = li.a.get('href')
            print(f' - {texto} -> {href}')
            diccionario_lis[texto] = href

    lista = [{'pelicula': k, 'link': v} for k, v in diccionario_lis.items()]

    archivo_json = archivo_salida.replace('.html', '.json')
    with open(archivo_json, 'w', encoding='utf8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=2)

    print(f'[✓] JSON guardado en {archivo_json} con {len(lista)} entradas.')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Scrapper para Wikipedia')
    parser.add_argument('--url', type=str, help='URL de la página de Wikipedia')
    parser.add_argument('--output', type=str, default='wiki.html')
    args = parser.parse_args()

    url = args.url or 'https://es.wikipedia.org/wiki/Categor%C3%ADa:Pel%C3%ADculas_de_terror_sobrenatural'
    output = args.output or 'wiki.html'

    main(url, output)
