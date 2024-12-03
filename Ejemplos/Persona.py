from Evento import *
from os import system

class Persona:
    def __init__(self, *args) -> None:
        argumentos = len(args)
        if argumentos>=6 and argumentos<= 11:
            self._Nombre = args[0]
            self._Paterno = args[1]
            self._Materno = args[2]
            self._Genero = args[3]
            self._estatura = args[4]
            if argumentos == 6:
                self._FechaNacimiento = args[5]
            elif argumentos == 7:
                self._FechaNacimiento = Evento(args[5], args[6])
            else:
                self._FechaNacimiento = Evento(args[5], args[6], args[7], args[8], args[9], args[10])
            self.verificaTuEstado()
        else:
            self._Nombre = ''
            self._Paterno = ''
            self._Materno = ''
            self._Genero = ''
            self._estatura = 0.24
            self._FechaNacimiento = Evento()

    def __del__(self):
        pass

    @property
    def Nombre(self):
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre):
        self._Nombre = Nombre
        self.verificaTuEstado()

    @property
    def Paterno(self):
        return self._Paterno
    
    @Paterno.setter
    def Paterno(self, Paterno):
        self._Paterno = Paterno
        self.verificaTuEstado()

    @property
    def Materno(self):
        return self._Materno
    
    @Materno.setter
    def Materno(self, Materno):
        self._Materno = Materno
        self.verificaTuEstado()

    @property
    def Genero(self):
        return self._Genero
    
    @Genero.setter
    def Genero(self, Genero):
        self._Genero = Genero
        self.verificaTuEstado()

    @property
    def estatura(self):
        return self._estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura
        self.verificaTuEstado()

    @property
    def FechaNacimiento(self):
        return self._FechaNacimiento
    
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento):
        self._FechaNacimiento = FechaNacimiento
        self.verificaTuEstado()

    def __str__(self) -> str:
        datos = f'Nombre: {self._Nombre}\n'
        datos += f'Paterno: {self._Paterno}\n'
        datos += f'Materno: {self._Materno}\n'
        datos += f'Genero: {self._Genero}\n'
        datos += f'estatura: {self._estatura}\n'
        datos += f'FechaNacimiento: {self._FechaNacimiento}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        self._Nombre = input('Dame mi Nombre ')
        self._Paterno = input('Dame mi Paterno ')
        self._Materno = input('Dame mi Materno ')
        self._Genero = input('Dame mi Genero ')
        self._estatura = input('Dame mi estatura ')
        print('Dame mi Fecha de Nacimiento')
        self._FechaNacimiento.pideleAlUsuarioTuEstado()
        self.verificaTuEstado()
    
    def muestraTuEstado(self):
        print(self)

    def modificaTuEstado(self, *args) -> None:
        self.__init__(*args)

    def verificaTuEstado(self):
        if not isinstance(self._Nombre,str):
            self._Nombre = ''
        if not isinstance(self._Paterno,str):
            self._Paterno = ''
        if not isinstance(self._Materno,str):
            self._Materno = ''
        if not isinstance(self._Genero,str):
            self._Genero = ''
        try:
            self._estatura = float(self._estatura)
        except:
            self._estatura = 0.24
        if self._estatura<0.24 or self._estatura>2.72:
            self._estatura = 0.24
        if not isinstance(self._FechaNacimiento, Evento):
            self._FechaNacimiento = Evento()

if __name__ == '__main__':
    system('cls')

    P1 = Persona()
    print(f'P1')
    P1.muestraTuEstado()

    FN = Evento(1,2,2003,4,5,6)
    P2 = Persona('Juan','Perez','Lopez','Masculino',1.65,FN)
    print(f'P2\n{P2}')

    FFN = Fecha(7,8,2009)
    HFN = Hora(10,11,12)
    P3 = Persona('Luisa','Garcia','Hernandez','Femenino',1.75,FFN, HFN)
    print(f'P3\n{P3}')

    P4 = Persona('Alfonso','Reyes','Ochoa','Masculino',1.82,17,5,1889,16,17,18)
    print(f'P4\n{P4}')

    print(f'P1\n{P1}')
    print(f'P1')
    P1.pideleAlUsuarioTuEstado()
    print(f'\nP1\n{P1}')

    print('Se intenta P1.modificaTuEstado()')
    P1.modificaTuEstado()
    print(f'\nP1\n{P1}')

    print('Se intenta P1.modificaTuEstado(1, 2.3, 4, 5.6, \'uno ochenta\', 789)')
    P1.modificaTuEstado(1, 2.3, 4, 5.6, 'uno ochenta', 789)
    print(f'\nP1\n{P1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    P1.Nombre = 1
    P1.Paterno = 2.3
    P1.Materno = 4
    P1.Genero = 5.6
    P1.estatura = 'uno ochenta'
    P1.FechaNacimiento = 789
    print(f'\nP1\n{P1}')
