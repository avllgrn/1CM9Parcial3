from os import system
from Punto2D import *
from math import fabs

class RectanguloP:
    def __init__(self, *args) -> None:
        cantidad = len(args)
        if cantidad == 2 and isinstance(args[0],Punto2D) and isinstance(args[1],Punto2D):
            self._P1 = args[0]
            self._P2 = args[1]
        elif cantidad == 4:
            self._P1 = Punto2D(args[0], args[1])
            self._P2 = Punto2D(args[2], args[3])
        else:
            self._P1 = Punto2D()
            self._P2 = Punto2D()
    
    def __del__(self) -> None:
        pass

    @property
    def P1(self):
        return self._P1

    @P1.setter
    def P1(self, P1):
        if isinstance(P1, Punto2D):
            self._P1 = P1
    
    @property
    def P2(self):
        return self._P2

    @P2.setter
    def P2(self, P2):
        if isinstance(P2, Punto2D):
            self._P2 = P2
    
    def __str__(self) -> str:
        datos = f'P1{self._P1}\n'
        datos += f'P2{self._P2}\n'
        datos += f'Base: {self.dameTuBase()}\n'
        datos += f'Altura: {self.dameTuAltura()}\n'
        datos += f'Área: {self.dameTuArea()}\n'
        datos += f'Perímetro: {self.dameTuPerimetro()}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        print('Dame mi P1')
        self._P1.pideleAlUsuarioTuEstado()
        print('Dame mi P2')
        self._P2.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args):
        self.__init__(*args)

    def dameTuBase(self):
        base = fabs(self._P1._x - self._P2._x)
        altura = fabs(self._P1._y - self._P2._y)
        if base>0 and altura>0:
            return base
        else:
            return 0

    def dameTuAltura(self):
        base = fabs(self._P1._x - self._P2._x)
        altura = fabs(self._P1._y - self._P2._y)
        if base>0 and altura>0:
            return altura
        else:
            return 0

    def dameTuArea(self):
        return self.dameTuBase() * self.dameTuAltura()

    def dameTuPerimetro(self):
        return 2*self.dameTuBase() + 2*self.dameTuAltura()

if __name__ == '__main__':
    system('cls')

    R1 = RectanguloP()
    print(f'R1\n{R1}')

    A = Punto2D(1,1)
    B = Punto2D(4,5)
    R2 = RectanguloP(A, B)
    print(f'R2')
    R2.muestraTuEstado()

    R3 = RectanguloP(5, 6, 7, 8)
    print(f'R3')
    R3.muestraTuEstado()

    print(f'R1')
    R1.pideleAlUsuarioTuEstado()
    print(f'R1\n{R1}')

    print('Se intenta construir un objeto con dos cadenas:')
    R4 = RectanguloP('unaCadena', 'otraCadena')
    print(f'R4\n{R4}')
    print('Se intenta modificar un objeto con cuatro cadenas:')
    R4.modificaTuEstado('cadena1', 'cadena2', 'cadena3', 'cadena4')
    print(f'R4\n{R4}')

    print('Se intenta construir un objeto con 4 cadenas:')
    R5 = RectanguloP('cadena1', 'cadena2', 'cadena3', 'cadena4')
    print(f'R5\n{R5}')

    print('Se intenta asignar una cadena al P1 de un objeto:')
    R4.P1 = '(1.2, 3.4)'
    print(f'R4\n{R4}')
    print('Se intenta asignar una cadena al P2 de un objeto:')
    R4.P2 = '(5.6, 7.8)'
    print(f'R4\n{R4}')
