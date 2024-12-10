from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    archivoSalida = open('datos.txt','w')

    for i in range(10):
        for j in range(10):
            archivoSalida.write(str(randrange(100)/10)+', ')
        archivoSalida.write('\n')

    archivoSalida.close()

    archivoEntrada = open('datos.txt','r')

    Matriz = []                         # Se genera una matriz (lista) vacía

    for linea in archivoEntrada:        # Se lee cada línea del archivo
        i = linea.split(',')            # Se parte cada línea en una lista de cadenas separadas por coma.
        renglon = []                    # Se genera un renglón vacío para la matríz

        for j in i:                     # Por cada cadena en la lista de cadenas,0
            try:                        # se intenta
                dato = float(j)         # convertir a flotante cada cadena
                renglon.append(dato)    # y agregarse al renglón.
            except:                     # En caso de no poderse convertir,
                pass                    # se continuá intentando
        Matriz.append(renglon)          #Al final, se agrega cada renglón a la matriz




    filas = len(Matriz)                     # Tamaño de la lista de listas
    columnas = len(Matriz[0])               # Tamaño de cualquiera de sus listas

    print(f'\nMatriz {filas}x{columnas}')
    print(Matriz)                           # Python muestra la matriz, lista de listas
    print()


    print(f'\nMatriz {filas}x{columnas}')
    for i in range(filas):                  # Cada lista, renglón por renglón,
        for j in range(columnas):           # elemento a elemento, columna por columna, de cada renglón
            print(Matriz[i][j], end='\t')   # es mostrado
        print()
