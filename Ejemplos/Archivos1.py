from os import system

if __name__ == '__main__':
    system('cls')

    archivoSalida = open('datos.txt','w')

    archivoSalida.write('Una linea de texto')
    archivoSalida.write('Otra linea de texto')
    archivoSalida.write('Linea de texto con numeros 1234')
    archivoSalida.write('Aunque hay numeros 1234, es una linea de texto')
    
    archivoSalida.close()
