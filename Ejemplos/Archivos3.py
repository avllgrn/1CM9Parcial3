from os import system

if __name__ == '__main__':
    system('cls')

    archivoSalida = open('datos.txt','w')

    contador = 0
    for i in range(10):
        for j in range(10):
            archivoSalida.write(str(contador)+', ')
            contador += 1
        archivoSalida.write('\n')

    archivoSalida.close()

