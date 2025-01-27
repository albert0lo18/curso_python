def Calcular_Y(x:float,m:float,b:float)->float:
    '''
    Calcula el valor de y en una linea recta 
    x: valor de x
    m: pendiente
    b: interseccion de y
    regresa el valor de y
    '''
    return (m*x)+b

def test_linea():
    '''
    Prueba de funcionamiento de 
    Calcular_Y
    '''
    x= Calcular_Y(0.0,2.0,3.0)
    if x==3.0:
        return True
    else:
        False
        
    
if __name__== '__main__':
    if test_linea():
        print('todobien')
    else:
        print('supu')