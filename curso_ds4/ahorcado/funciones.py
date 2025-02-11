def carga_archivo_texto(archivo: str) -> list:
    '''
    Carga un archivo de texto y devuelve una lista de oraciones
    '''
    with open(archivo, 'r', encoding= 'utf-8') as file:
        oraciones = file.readlines()
    return oraciones

def carga_plantillas(nombre_plantilla: str) -> dict:
    '''
    Carga plantillas del juego a partir de un archivo de texto
    '''
    plantillas = {}
    for i in range(6):
        plantillas[i] = carga_archivo_texto(f'./plantillas/{nombre_plantilla}-{i}.txt')
    return plantillas

def despliega_plantilla(diccionario:dict, nivel:int):
    '''
    Despliega una plantilla del ahorcado
    
    '''
    plantilla = diccionario[nivel]
    for renglon in plantilla:
        print(renglon)   


if __name__ == '__main__':
    plantilla = carga_plantillas('plantilla')
    despliega_plantilla(plantilla, 5)
    Lista_oraciones = carga_archivo_texto('./datos/pg15532.txt')
    print(Lista_oraciones[110:115])
