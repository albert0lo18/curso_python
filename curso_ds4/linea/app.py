import funciones
import argparse
 
def main(m:float, b:float):
    # X =[x for x in range(1,11)]
    # Y =[funciones.Calcular_Y(x,m,b) for x in X]
    # print('Enteros:')
    # coordenadas_enteros = list(zip(X,Y))
    # print(coordenadas_enteros)
    XF = [x/10.0 for x in range(10,110,5)]
    YF = [funciones.Calcular_Y(x,m,b) for x in XF]
    coordenadas_flotantes = list(zip(XF,YF))
    print('Flotantes')
    print(coordenadas_flotantes)
 
if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument ('-m', type=float, help='pendiente de la recta', default=2.0)
    parser.add_argument ('-b', type=float, help='ordenada de la recta', default=3.0)
    args = parser.parse_args()
    main(args.m, args.b)
    
    