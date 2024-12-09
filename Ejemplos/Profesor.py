from Empleado import *
from os import system

class Profesor (Empleado):
    def __init__(self, *args) -> None:
        argumentos = len(args)
        if argumentos <12 or argumentos > 17:
            super().__init__()
            self._numeroGrupos = 0
            self._carga = 0.0
            self._Academia = 'Trabajador'
        else:
            if argumentos == 12:
                super().__init__(*args[0:9])
            elif argumentos == 13:
                super().__init__(*args[0:10])
            elif argumentos == 17:
                super().__init__(*args[0:14])
            self._numeroGrupos = args[-3]
            self._carga = args[-2]
            self._Academia = args[-1]
            self.verificaProfesor()

    def __del__(self):
        pass

    @property
    def numeroGrupos(self):
        return self._numeroGrupos

    @numeroGrupos.setter
    def numeroGrupos(self, numeroGrupos):
        self._numeroGrupos = numeroGrupos
        self.verificaProfesor()

    @property
    def carga(self):
        return self._carga

    @carga.setter
    def carga(self, carga):
        self._carga = carga
        self.verificaProfesor()

    @property
    def Academia(self):
        return self._Academia

    @Academia.setter
    def Academia(self, Academia):
        self._Academia = Academia
        self.verificaProfesor()

    def __str__(self) -> str:
        datos = super().__str__()
        datos += f'Numero de grupos: {self._numeroGrupos}\n'
        datos += f'Carga: {self._carga}\n'
        datos += f'Academia: {self._Academia}\n'
        return datos
    
    def pideleAlUsuarioTuEstado(self):
        super().pideleAlUsuarioTuEstado()
        self._numeroGrupos = input('Dame mi número de grupos ')
        self._carga = input('Dame mi carga ')
        self._Academia = input('Dame mi academia ')
        self.verificaProfesor()

    def muestraTuProfstado(self):
        print(self)

    def modificaProfesor(self, *args) -> None:
        self.__init__(*args)

    def verificaProfesor(self):
        if not isinstance(self._Academia,str):
            self._Academia = 'Computación'

        try:
            self._numeroGrupos = int(self._numeroGrupos)
        except:
            self._numeroGrupos = 0
        try:
            self._carga = float(self._carga)
        except:
            self._carga = 0.0

        if self._numeroGrupos < 0:
            self._numeroGrupos = 0

        if self._carga < 0.0 and self._carga > 24.0:
            self._carga = 0.0

if __name__ == '__main__':
    system('cls')

    Prof1 = Profesor()
    print(f'Prof1')
    Prof1.muestraTuProfstado()

    FN = Evento(1,2,2003,4,5,6)
    Prof2 = Profesor('Juan','Perez','Lopez','m',1.82,FN,2,4967.6,'Docente', 1, 1.5, 'Humanidades')
    print(f'Prof2\n{Prof2}')

    FFN = Fecha(7,8,2009)
    HFN = Hora(10,11,12)
    Prof3 = Profesor('Mario','Almada','Juarez','masc.',1.76,FFN,HFN,3,5678.9,'Profesor', 3, 4.5, 'Electrónica')
    print(f'Prof3\n{Prof3}')

    Prof4 = Profesor('Laura','Zuniga','Ruiz','Fem.',1.86,29,4,2004,8,54,32,4,49876.54,'Maestro', 5, 7.5, 'Circuitos')
    print(f'Prof4\n{Prof4}')

    Prof5 = Profesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'siete', 'Diez punto cinco', 3.1416)
    print(f'Prof5\n{Prof5}')

    print(f'Prof1\n{Prof1}')
    print(f'Prof1')
    Prof1.pideleAlUsuarioTuEstado()
    print(f'\nProf1\n{Prof1}')    

    print('Se intenta P1.modificaProfesor()')
    Prof1.modificaProfesor()
    print(f'\nProf1\n{Prof1}')

    print('Se intenta Prof1.modificaProfesor(1, 2.3, 4, 5.6, \'uno ochenta\', 789, \'mil\', \'un millón\', 56.78, \'dos\', \'tres\', 2.71)')
    Prof1.modificaProfesor(1, 2.3, 4, 5.6, 'uno ochenta', 789, 'mil', 'un millón', 56.78, 'dos', 'tres', 2.71)
    print(f'\nProf1\n{Prof1}')

    print('Se intenta asignar valores incorrectos a los atributos')
    Prof1.Nombre = 1
    Prof1.Paterno = 2.3
    Prof1.Materno = 4
    Prof1.Genero = 5.6
    Prof1.estatura = 'uno ochenta'
    Prof1.FechaNacimiento = 789
    Prof1.numeroEmpleado = 'uno dos tres cuatro'
    Prof1.sueldo = 'siete mil cuatrocientos sesenta y siete punto nueve'
    Prof1.Puesto = 456.654
    Prof1.numeroGrupos = 'cinco'
    Prof1.carga = 'siete punto cinco'
    Prof1.Academia = 9.81
    print(f'\nProf1\n{Prof1}')
