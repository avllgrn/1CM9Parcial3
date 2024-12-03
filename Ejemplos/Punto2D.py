from os import system
from math import sqrt, pow

class Punto2D:

    def __init__(self, _x=0.0, _y=0.0):
        try:
            self._x = float(_x)
            self._y = float(_y)
        except:
            self._x = 0.0
            self._y = 0.0

    def __del__(self):
        pass

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        try:
            self._x = float(x)
        except:
            self._x = 0.0

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        try:
            self._y = float(y)
        except:
            self._y = 0.0

    def __str__(self):
        return f'({self._x}, {self._y})'

    def pideleAlUsuarioTuEstado(self):
        try:
            self._x = float(input('Dame mi x '))
        except:
            self._x = 0.0
        try:
            self._y = float(input('Dame mi y '))
        except:
            self._y = 0.0

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, _x, _y):
        self.__init__(_x,_y)

    def guardaTuEstado(self, ArchivoSalida):
        ArchivoSalida.write(f'{self._x},{self._y}')

    def cargaTuEstado(self,ArchivoEntrada):
        datos = ArchivoEntrada.readline().split(',')
        try:
            self._x = float(datos[0])
        except:
            self._x = 0.0
        try:
            self._y = float(datos[1])
        except:
            self._y = 0.0

    def __add__(self, Derecho):
        R = None
        if isinstance(Derecho, Punto2D):
            R = Punto2D()
            R.modificaTuEstado(self._x + Derecho._x, self._y + Derecho._y)
        return R

    def __sub__(self, Derecho):
        R = None
        if isinstance(Derecho, Punto2D):
            R = Punto2D()
            R.modificaTuEstado(self._x - Derecho._x, self._y - Derecho._y)
        return R
    
def calculaPendiente(A, B):
    d = (B._x - A._x)
    if type(A) == type(B) and isinstance(A, Punto2D) and d != 0:
        return (B._y - A._y) / (B._x - A._x)
    else:
        return None

def calculaDistancia(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return sqrt(pow(B._x - A._x, 2) + pow(B._y - A._y, 2))
    else:
        return None

def suma(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return A+B
    else:
        return None

def resta(A, B):
    if type(A) == type(B) and isinstance(A, Punto2D):
        return A-B
    else:
        return None


if __name__ == '__main__':
    system('cls')
    P = Punto2D()
    Q = Punto2D()
    S = Punto2D()
    R = Punto2D()

    print(f'P',end='')
    P.muestraTuEstado()
    print(f'Q',end='')
    Q.muestraTuEstado()
    print(f'P{P}')
    print(f'Q{Q}\n')

    print(f'P')
    P.pideleAlUsuarioTuEstado()
    print(f'Q')
    Q.pideleAlUsuarioTuEstado()

    d = calculaDistancia(P, Q)
    m = calculaPendiente(P, Q)
    S = suma(P, Q)
    R = resta(P, Q)

    print(f'P{P}')
    print(f'Q{Q}')
    print(f'd = {d}')
    print(f'm = {m}')
    print(f'S{S}')
    print(f'R{R}\n')
