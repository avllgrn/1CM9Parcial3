from os import system
from Fecha import *
from Hora import *

class Evento:
    def __init__(self, *args) -> None:
        argumentos = len(args)
        if argumentos == 0:
            self._F = Fecha()
            self._H = Hora()
        elif argumentos == 2:
            if isinstance(args[0], Fecha):
                self._F = args[0]
            else:
                self._F = Fecha()
            if isinstance(args[1], Hora):
                self._H = args[1]
            else:
                self._H = Hora()
        else:
            self._F = Fecha(args[0], args[1], args[2])
            self._H = Hora(args[3], args[4], args[5])

    def __del__(self):
        pass

    @property
    def F(self):
        return self._F
    
    @F.setter
    def F(self, F):
        if isinstance(F, Fecha):
            self._F = F

    @property
    def H(self):
        return self._H
    
    @H.setter
    def H(self, H):
        if isinstance(H, Hora):
            self._H = H

    def __str__(self) -> str:
        return f'{self._F} {self._H}'

    def pideleAlUsuarioTuEstado(self):
        print('Dame mi F ')
        self._F.pideleAlUsuarioTuEstado()
        print('Dame mi H')
        self._H.pideleAlUsuarioTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args):
        self.__init__(*args)

if __name__ == '__main__':
    system('cls')

    print('Se intenta construir una instancia de Evento con dos cadenas:')
    UnaFecha = 'Fecha(1, 2, 3)'
    UnaHora = 'Hora(4, 5, 6)'
    E1 = Evento(UnaFecha, UnaHora)
    print(f'E1 -> {E1}\n')

    print('Se intenta construir una instancia de Evento con seis cadenas:')
    E2 = Evento('cuatro', 'cinco', 'seis', 'una', 'dos', 'tres')
    print(f'E2 -> {E2}\n')

    print('Se intenta modificar una instancia de Evento con dos cadenas:')
    E1.modificaTuEstado(UnaFecha, UnaHora)
    print(f'E1 -> {E1}\n')

    print('Se intenta modificar una instancia de Evento con seis cadenas:')
    E2.modificaTuEstado('cuatro', 'cinco', 'seis', 'una', 'dos', 'tres')
    print(f'E2 -> {E2}\n')

    print('Se intenta asignar cadenas a los atributos de una instancia de Evento:')
    E1.F = 'Fecha(1, 2, 3)'
    E1.H = 'Hora(4, 5, 6)'
    print(f'E1 -> {E1}\n')
