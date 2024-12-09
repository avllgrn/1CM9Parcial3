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
            self.verificaPersona()
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
        self.verificaPersona()

    @property
    def Paterno(self):
        return self._Paterno
    
    @Paterno.setter
    def Paterno(self, Paterno):
        self._Paterno = Paterno
        self.verificaPersona()

    @property
    def Materno(self):
        return self._Materno
    
    @Materno.setter
    def Materno(self, Materno):
        self._Materno = Materno
        self.verificaPersona()

    @property
    def Genero(self):
        return self._Genero
    
    @Genero.setter
    def Genero(self, Genero):
        self._Genero = Genero
        self.verificaPersona()

    @property
    def estatura(self):
        return self._estatura
    
    @estatura.setter
    def estatura(self, estatura):
        self._estatura = estatura
        self.verificaPersona()

    @property
    def FechaNacimiento(self):
        return self._FechaNacimiento
    
    @FechaNacimiento.setter
    def FechaNacimiento(self, FechaNacimiento):
        self._FechaNacimiento = FechaNacimiento
        self.verificaPersona()

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
        self.verificaPersona()
    
    def muestraTuEstado(self):
        print(self)

    def modificaPersona(self, *args) -> None:
        self.__init__(*args)

    def verificaPersona(self):
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
    print(f'P1\n{P1}')

    E = Evento(29,11,2024, 10, 18, 34)
    P2 = Persona('Juan','Perez','Lopez','Masculino',1.65, E)
    print(f'P2')
    P2.muestraTuEstado()

    UnaFecha = Fecha(2,12,2024)
    UnaHora = Hora(7,10,32)
    P3 = Persona('Luisa','Garcia','Hernandez','Femenino',1.75, UnaFecha, UnaHora)
    print(f'P3\n{P3}')

    P4 = Persona('Alfonso','Reyes','Ochoa','Masculino',1.82,17,5,1889,16,17,18)
    print(f'P4\n{P4}')

    print(f'P1\n{P1}')
    P1.pideleAlUsuarioTuEstado()
    print(f'\nP1\n{P1}')

    print('Se realiza P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)')
    P1.modificaPersona(P2.Nombre, P2.Paterno, P2.Materno, P2.Genero, P2.estatura, P2.FechaNacimiento)
    print(f'P2\n{P2}')
    print(f'P1\n{P1}')

    print('Se realiza P1.modificaPersona(P3.Nombre, P3.Paterno, P3.Materno, P3.Genero, P3.estatura, P3.FechaNacimiento.F, P3.FechaNacimiento.H)')
    P1.modificaPersona(P3.Nombre, P3.Paterno, P3.Materno, P3.Genero, P3.estatura, P3.FechaNacimiento.F, P3.FechaNacimiento.H)
    print(f'P3\n{P3}')
    print(f'P1\n{P1}')

    print('Se realiza P1.modificaPersona(P4.Nombre, P4.Paterno, P4.Materno, P4.Genero, P4.estatura, P4.FechaNacimiento.F.dia, P4.FechaNacimiento.F.mes, P4.FechaNacimiento.F.anio, P4.FechaNacimiento.H.hora, P4.FechaNacimiento.H.minuto, P4.FechaNacimiento.H.segundo)')
    P1.modificaPersona(P4.Nombre, P4.Paterno, P4.Materno, P4.Genero, P4.estatura, P4.FechaNacimiento.F.dia, P4.FechaNacimiento.F.mes, P4.FechaNacimiento.F.anio, P4.FechaNacimiento.H.hora, P4.FechaNacimiento.H.minuto, P4.FechaNacimiento.H.segundo)
    print(f'P4\n{P4}')
    print(f'P1\n{P1}')

    print('Se intenta Persona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P5 = Persona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P5\n{P5}')

    print('Se intenta P5.modificaPersona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123, 456)')
    P5.modificaPersona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123, 456)
    print(f'P5\n{P5}')

    print('Se intenta P5.modificaPersona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', 123)')
    P5.modificaPersona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', 123)
    print(f'P5\n{P5}')

    print('Se intenta P5.modificaPersona(12.3, 45.6, 78.9, 8.76, \'uno sesenta\', \'1.2\', \'3.4\', \'5.6\', \'7.8\', \'9.8\', \'7.6\')')
    P5.modificaPersona(12.3, 45.6, 78.9, 8.76, 'uno sesenta', '1.2', '3.4', '5.6', '7.8', '9.8', '7.6')
    print(f'P5\n{P5}')

    print('Se intenta asignar valores incorrectos a los atributos de P5')
    P5.Nombre = 12.3
    P5.Paterno = 45.6
    P5.Materno = 78.9
    P5.Genero = 8.76
    P5.estatura = 'uno sesenta'
    P5.FechaNacimiento = 123
    print(f'P5\n{P5}')
