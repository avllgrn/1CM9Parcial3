from os import system
from Punto2D import *
from math import pi

class CirculoP:
    def __init__(self, *args) -> None:
        cantidad = len(args)
        if cantidad == 2 and isinstance(args[0],Punto2D) and isinstance(args[1],Punto2D):
            self._C = args[0]
            self._P = args[1]
        elif cantidad == 4:
            self._C = Punto2D(args[0], args[1])
            self._P = Punto2D(args[2], args[3])
        else:
            self._C = Punto2D()
            self._P = Punto2D()
    
    def __del__(self) -> None:
        pass

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, C):
        if isinstance(C, Punto2D):
            self._C = C
    
    @property
    def P(self):
        return self._P

    @P.setter
    def P(self, P):
        if isinstance(P, Punto2D):
            self._P = P
    
    def __str__(self) -> str:
        datos = f'C{self._C}\n'
        datos += f'P{self._P}\n'
        datos += f'Radio: {self.dameTuRadio()}\n'
        datos += f'Diametro: {self.dameTuDiametro()}\n'
        datos += f'Área: {self.dameTuArea()}\n'
        datos += f'Perímetro: {self.dameTuPerimetro()}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        print('Dame mi C')
        self._C.pideleAlUsuarioTuEstado()
        print('Dame mi P')
        self._P.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args):
        self.__init__(*args)

    def dameTuRadio(self):
        return calculaDistancia(self._C, self._P)    

    def dameTuDiametro(self):
        return 2*self.dameTuRadio()

    def dameTuArea(self):
        return pi*self.dameTuRadio()**2

    def dameTuPerimetro(self):
        return 2*pi*self.dameTuRadio()

if __name__ == '__main__':
    system('cls')

    Q1 = CirculoP()
    print(f'Q1\n{Q1}')

    A = Punto2D(1,1)
    B = Punto2D(2,2)
    Q2 = CirculoP(A, B)
    print(f'Q2')
    Q2.muestraTuEstado()

    Q3 = CirculoP(5.5, 6.6, 7.7, 8.8)
    print(f'Q3')
    Q3.muestraTuEstado()

    print(f'Q1')
    Q1.pideleAlUsuarioTuEstado()
    print(f'Q1\n{Q1}')

    print('Se intenta construir un objeto con dos cadenas:')
    Q4 = CirculoP('unaCadena', 'otraCadena')
    print(f'Q4\n{Q4}')
    print('Se intenta modificar un objeto con cuatro cadenas:')
    Q4.modificaTuEstado('cadena1', 'cadena2', 'cadena3', 'cadena4')
    print(f'Q4\n{Q4}')

    print('Se intenta construir un objeto con 4 cadenas:')
    Q5 = CirculoP('cadena1', 'cadena2', 'cadena3', 'cadena4')
    print(f'Q5\n{Q5}')

    print('Se intenta asignar una cadena al C de un objeto:')
    Q4.C = '(1.2, 3.4)'
    print(f'Q4\n{Q4}')
    print('Se intenta asignar una cadena al P de un objeto:')
    Q4.P = '(5.6, 7.8)'
    print(f'Q4\n{Q4}')
