from os import system

class Fecha:
    def __init__(self, dia=1, mes=1, anio=2024):
        self._dia = dia
        self._mes = mes
        self._anio = anio
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        return f'{self._dia}/{self._mes}/{self._anio}'
    
    @property
    def dia(self):
        return self._dia

    @dia.setter
    def dia(self, dia):
        self._dia = dia
        self.verificaTuEstado()

    @property
    def mes(self):
        return self._mes

    @mes.setter
    def mes(self, mes):
        self._mes = mes
        self.verificaTuEstado()

    @property
    def anio(self):
        return self._anio

    @anio.setter
    def anio(self, anio):
        self._anio = anio
        self.verificaTuEstado()

    def pideleAlUsuarioTuEstado(self):
        self._dia = input('Dame mi dia ')
        self._mes = input('Dame mi mes ')
        self._anio = input('Dame mi anio ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args):
        self.__init__(*args)

    def verificaTuEstado(self):
        try:
            self._dia = int(self._dia)
        except:
            self._dia = 1
        try:
            self._mes = int(self._mes)
        except:
            self._mes = 1
        try:
            self._anio = int(self._anio)
        except:
            self._anio = 2024

        if self._anio<0:
            self._anio=2024

        if self._mes<1 or self._mes>12:
            self._mes=1
        
        if self._dia<1 or self._dia>31:
            self._dia=1

if __name__ == '__main__':
    system('cls')

    print('Se intenta construir una instancia de Fecha con cadenas:')
    F = Fecha('cinco', 'mayo', 'dos mil veinte')
    print(f'F -> {F}\n')

    print('Se intenta modificar una instancia de Fecha con cadenas:')
    F.modificaTuEstado('primero', 'abril', 'dos mil veinticuatro')
    print(f'F -> {F}\n')

    print('Se intenta asignar cadenas a los atributos de una instancia de Fecha:')
    F.dia = 'cinco'
    F.mes = 'mayo'
    F.anio = 'dos mil ocho'
    print(f'F -> {F}\n')

    print('Si se intenta ingresar cadenas a los atributos de una instancia de Fecha:')
    F.pideleAlUsuarioTuEstado()
    print(f'F -> {F}\n')
