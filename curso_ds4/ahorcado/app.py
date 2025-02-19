import funciones as fn
from random import choice
import string


def main(archivo_texto:str, nombre_plantilla='plantilla'):
    '''
    programa principal
    '''

    #cargamos plantillas
    plantillas = fn.carga_plantillas(nombre_plantilla)
    Lista_oraciones = fn.carga_archivo_texto(archivo_texto)
    palabras = fn.obten_palabras(Lista_oraciones)
    p= choice(palabras) 
    abcdario = {letra:letra for letra in string.ascii_lowercase}
    letras_adivinadas = set()
    
    o= 10 # oportunidades 
    while o > 0:
        o= fn.adivina_letra(abcdario, p, letras_adivinadas, o)
        print(o)
        fn.despliega_plantilla(plantillas,o)
        fn.adivina_letra(abcdario,p,letras_adivinadas,o)
        if p ==''.join(letra if letra in letras_adivinadas else '_' for letra in p):
            print('ganaste')
            break
    fn.despliega_plantilla(plantillas, o)
    print(f"la palabra era: {p}")    
    
    
if __name__ == '__main__':
    archivo = './datos/pg15532.txt'
    main(archivo)
    
    