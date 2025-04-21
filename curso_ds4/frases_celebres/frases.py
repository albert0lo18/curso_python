import csv
import argparse

# Cargar el archivo CSV con las frases y las películas
def cargar_datos(csv_file):
    frases_peliculas = []
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Saltar la cabecera
        for row in reader:
            frase = row[0]
            pelicula = row[1]
            frases_peliculas.append((frase, pelicula))
    return frases_peliculas

# Función para buscar la película con las palabras
def buscar_pelicula_por_palabras(palabras_buscadas, frases_peliculas):
    peliculas_encontradas = set()  # Usamos un set para evitar duplicados
    for frase, pelicula in frases_peliculas:
        for palabra in palabras_buscadas:
            if palabra.lower() in frase.lower():
                peliculas_encontradas.add(pelicula)  # Añadir la película si encontramos la palabra
                break  # Salir del bucle una vez que encontramos la palabra en la frase
    
    if peliculas_encontradas:
        return peliculas_encontradas
    else:
        return "No se encontró ninguna película con esas palabras."

# Main
def main():
    # Crear un parser para los argumentos
    parser = argparse.ArgumentParser(description="Buscar películas por palabras.")
    parser.add_argument('palabras', nargs='+', help="Palabras a buscar en las frases de las películas.")
    
    # Obtener los argumentos
    args = parser.parse_args()
    
    archivo_csv = 'frases.csv'  # Reemplaza con la ruta de tu archivo CSV
    frases_peliculas = cargar_datos(archivo_csv)
    
    # Obtener las palabras de los argumentos
    palabras_buscadas = args.palabras
    
    peliculas = buscar_pelicula_por_palabras(palabras_buscadas, frases_peliculas)
    
    if isinstance(peliculas, set):
        print(f"Las películas que contienen alguna de las palabras {', '.join(palabras_buscadas)} son:")
        for pelicula in peliculas:
            print(f"- {pelicula}")
    else:
        print(peliculas)

if __name__ == "__main__":
    main()
