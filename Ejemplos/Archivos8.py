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

    for linea in archivoEntrada:    # Se lee cada línea del archivo
        print('\n',linea, end='')   # Se muestra en consola cada línea del archivo
        print()
