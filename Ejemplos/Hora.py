from os import system

class Hora:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo
        self.verificaTuEstado()

    def __del__(self):
        pass

    def __str__(self):
        return f'{self._hora}:{self._minuto}:{self._segundo}'
    
    @property
    def hora(self):
        return self._hora

    @hora.setter
    def hora(self, hora):
        self._hora = hora
        self.verificaTuEstado()

    @property
    def minuto(self):
        return self._minuto

    @minuto.setter
    def minuto(self, minuto):
        self._minuto = minuto
        self.verificaTuEstado()

    @property
    def segundo(self):
        return self._segundo

    @segundo.setter
    def segundo(self, segundo):
        self._segundo = segundo
        self.verificaTuEstado()

    def pideleAlUsuarioTuEstado(self):
        self._hora = input('Dame mi hora ')
        self._minuto = input('Dame mi minuto ')
        self._segundo = input('Dame mi segundo ')
        self.verificaTuEstado()

    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args):
        self.__init__(*args)

    def verificaTuEstado(self):
        try:
            self._hora = int(self._hora)
        except:
            self._hora = 0
        try:
            self._minuto = int(self._minuto)
        except:
            self._minuto = 0
        try:
            self._segundo = int(self._segundo)
        except:
            self._segundo = 0

        if self._hora<0 or self._hora>23:
            self._hora=0

        if self._minuto<0 or self._minuto>59:
            self._minuto=0

        if self._segundo<0 or self._segundo>59:
            self._segundo=0


if __name__ == '__main__':
    system('cls')

    print('Se intenta construir una instancia de Hora con cadenas:')
    H = Hora('cinco', 'veinte', 'doce')
    print(f'H -> {H}\n')

    print('Se intenta modificar una instancia de Hora con cadenas:')
    H.modificaTuEstado('dos', 'catorce', 'cincuenta')
    print(f'H -> {H}\n')

    print('Se intenta asignar cadenas a los atributos de una instancia de Hora:')
    H.hora = 'una'
    H.minuto = 'once'
    H.segundo = 'cincuenta y tres'
    print(f'H -> {H}\n')

    print('Si se intenta ingresar cadenas a los atributos de una instancia de Hora:')
    H.pideleAlUsuarioTuEstado()
    print(f'H -> {H}\n')
