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

def juegos(simbolos:dict):
    ''' juego del gato '''
    
    print('juego del gato')
    
    lista_combinaciones = [
        ['1','2','3'],
        ['4','5','6'],
        ['7','8','9'],
        ['1','4','7'],
        ['2','5','8'],
        ['3','6','9'],
        ['1','5','9'],
        ['3','5','7']
    ]
    
    en_juego=True
    
    ganador = ""
    
    movimientos = 0
    
    dibuja_tablero(simbolos)
    
    while en_juego:
        
        usuario(simbolos)
        dibuja_tablero(simbolos)
        movimientos+=1
        ganador = checa_winner(simbolos, lista_combinaciones)
        if ganador is not None: 
            en_juego=False
            continue
        if movimientos >= 9:
            en_juego=False
            continue
              
        ia(simbolos)
        dibuja_tablero(simbolos)
        movimientos+=1
        ganador = checa_winner(simbolos, lista_combinaciones)
        if ganador is not None:
            en_juego=False
            continue
        
        if movimientos >= 9:
            en_juego=False
            continue
    
    return ganador     

def checa_winner (simbolos:dict, combinaciones:list):
    '''checa si hay un ganador'''
    for combinacion in combinaciones:
        if simbolos[combinacion[0]] == simbolos[combinacion[1]] == simbolos[combinacion[2]]!= ' ':
            return simbolos[combinacion[0]]
    return None

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

    