import tablero
def main():
    numeros = [str(x) for x in range(1,10)]
    simbolos = {x:x for x in numeros}
    ganador = tablero.juegos(simbolos)
    
    if ganador is not None:
        print (f'el ganador es: {ganador}')
    else:
        print('El juego es empate!')
        
if __name__ == '__main__':
    main()