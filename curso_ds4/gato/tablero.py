import random

#dibuja un tablero del juego del gato

def dibuja_tablero(simbolos:dict):
    '''
    dibuja el tablero del juego del gato
    '''
    print(f'''
     { simbolos['1']} | {simbolos['2']} | {simbolos['3']}
    -----------
     { simbolos['4']} | {simbolos['5']} | {simbolos['6']}
    -----------
     {simbolos['7']} | {simbolos['8']} | {simbolos['9']}   
    ''')

def ia(simbolos:dict):
    '''juega la maquina'''
    ocupado = True
    while ocupado is True:
        x=random.choice(list(simbolos.keys()))
        if simbolos[x] not in ['X', 'O']:
            simbolos[x] = 'O'
            ocupado = False

def usuario(simbolos:dict):
    ''' el usuario juega'''
    ocupado = True
    lista_numeros = [str(x) for x in range(1,10)]
    while ocupado is True:
        x = input('Ingrese la posicion (1-9): ')
        if x in lista_numeros:
            if simbolos[x] not in ['X', 'O']:
               simbolos[x] = 'X'
               ocupado = False
            else:
                print('Posicion invalida, intente nuevamente.')
        else: 
            print('Debe ingresar un NUMERO del 1 al 9.')

if __name__ == '__main__':
    numeros = [str(x) for x in range(1,10)]
    simbolos = {x:x for x in numeros}
    print('Bienvenido al juego del gato!')
    dibuja_tablero(simbolos)
    ia(simbolos)
    dibuja_tablero(simbolos)
    usuario(simbolos)
    dibuja_tablero(simbolos)
    '''
    X=random.choice(numeros)
    numeros.remove(X)
    simbolos[X] = 'X'
    dibuja_tablero(simbolos)
    O=random.choice(numeros)
    numeros.remove(O)
    simbolos[O] = 'O'
    dibuja_tablero(simbolos)
    print(numeros)
    '''
    

    