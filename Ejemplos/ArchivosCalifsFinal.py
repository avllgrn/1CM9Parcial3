from os import system
from random import randrange

if __name__ == '__main__':
    system('cls')

    alumnos = int(input('Cuántos alumnos? '))
    parciales = int(input('Cuántos parciales? '))
    nombreArchivo = input('Dónde se guardará? ')
    system('cls')

    # Se genera matriz con calificaciones aleatorias entre 0 y 10
    Matriz = []
    for alumno in range(alumnos):
        renglon = []
        for parcial in range(parciales):
            renglon.append(randrange(101)/10)
        Matriz.append(renglon)

    # Se almacena matriz con calificaciones aleatorias entre 0 y 10, en un archivo
    with open(nombreArchivo, 'w') as Archivo:
        for alumno in range(alumnos):
            for parcial in range(parciales):
                Archivo.write(str(Matriz[alumno][parcial])+', ')
            Archivo.write('\n')


    # Se carga matriz con calificaciones aleatorias entre 0 y 10, desde un archivo
    with open(nombreArchivo, 'r') as Archivo:
        Calificaciones = []
        for renglon in Archivo:
            alumno = []
            datos = renglon.split(',')
            for dato in datos:
                try:
                    alumno.append(float(dato))
                except:
                    pass
            Calificaciones.append(alumno)


    m = len(Calificaciones)
    n = len(Calificaciones[0])

    # Se agrega columna para promedios, a cada alumno en la matriz de calificaciones
    for i in range(m):
        Calificaciones[i].append(0.0)

    for i in range(m):                                      # Para cada alumno,
        for j in range(n):                                  # cada parcial,
            Calificaciones[i][n] += Calificaciones[i][j]    # se acumula en la nueva columna y, despues, 
        Calificaciones[i][n] /= n                           # se divide entre la cantidad de parciales

    # Se muestra el numero de parciales:
    print('Alumno',end='\t|')
    for j in range(n):
        print(f'P{j+1}',end='\t')
    print('Promedio\n')

    # Se muestra matriz cargada con calificaciones aleatorias entre 0 y 10
    for i in range(m):
        print(i+1,end='\t|')     # numero de alumno
        for j in range(n + 1):  # Ahora hay una columna extra (para calificaciones finales)
            print(Calificaciones[i][j],end='\t')
        print()
    print()

    # Se busca la menor calificacion en todos los parciales
    alumnoMenorParcial = 0
    examenMenorParcial = 0
    calificacionMenorParcial = Calificaciones[alumnoMenorParcial][examenMenorParcial]   # Se supone que el primer alumno en el primer parcial saco la menor calificiacion
    alumnoMayorParcial = 0
    examenMayorParcial = 0
    calificacionMayorParcial = Calificaciones[alumnoMayorParcial][examenMayorParcial]   # Se supone que el primer alumno en el primer parcial saco la menor calificiacion
    for i in range(m):                                                                  # Para cada alumno,
        for j in range(n):                                                              # cada parcial,

            if Calificaciones[i][j] < calificacionMenorParcial:                         # se comparan las calificaciones contra la supuesta menor
                    alumnoMenorParcial = i                                                              # Se guarda el numero de alumno
                    examenMenorParcial = j                                                              # Se guarda el numero de examen
                    calificacionMenorParcial = Calificaciones[alumnoMenorParcial][examenMenorParcial]   # Se guarda la nueva calificacion menor supuesta

            if Calificaciones[i][j] > calificacionMayorParcial:                         # se comparan las calificaciones contra la supuesta mayor
                    alumnoMayorParcial = i                                                              # Se guarda el numero de alumno
                    examenMayorParcial = j                                                              # Se guarda el numero de examen
                    calificacionMayorParcial = Calificaciones[alumnoMayorParcial][examenMayorParcial]   # Se guarda la nueva calificacion mayor supuesta

    print(f'El alumno {alumnoMenorParcial+1}, en el paricial {examenMenorParcial+1} tiene la calificacion más baja de todos los parciales: {calificacionMenorParcial}')
    print(f'El alumno {alumnoMayorParcial+1}, en el paricial {examenMayorParcial+1} tiene la calificacion más alta de todos los parciales: {calificacionMayorParcial}')

    # Se cuentan los alumnos aprobados y reprobados del semestre
    aprobadosSemestre = 0
    reprobadosSemestre = 0
    for i in range(m):

        if Calificaciones[i][n] >= 6:
            aprobadosSemestre += 1

        if Calificaciones[i][n] < 6:
            reprobadosSemestre += 1

    print(f'En el semestre, aprobaron {aprobadosSemestre} alumnos')
    print(f'En el semestre, reprobaron {reprobadosSemestre} alumnos\n')

    # Del primer parcial, se busca la menor y mayor calificacion, y se cuentan los aprobados y reproados
    alumnoMenorPrimerParcial = 0
    calificacionMenorPrimerParcial = Calificaciones[alumnoMenorPrimerParcial][0]
    alumnoMayorPrimerParcial = 0
    calificacionMayorPrimerParcial = Calificaciones[alumnoMayorPrimerParcial][0]
    aprobadosPrimerParcial = 0
    reprobadosPrimerParcial = 0

    for i in range(m):

        if Calificaciones[i][0] < calificacionMenorPrimerParcial:
            alumnoMenorPrimerParcial = i
            calificacionMenorPrimerParcial = Calificaciones[alumnoMenorPrimerParcial][0]

        if Calificaciones[i][0] > calificacionMayorPrimerParcial:
            alumnoMayorPrimerParcial = i
            calificacionMayorPrimerParcial = Calificaciones[alumnoMayorPrimerParcial][0]

        if Calificaciones[i][0] >= 6:
            aprobadosPrimerParcial += 1

        if Calificaciones[i][0] < 6:
            reprobadosPrimerParcial += 1

    print(f'En el primer paricial, el alumno {alumnoMenorPrimerParcial+1} tiene la calificacion más baja: {calificacionMenorPrimerParcial}')
    print(f'En el primer paricial, el alumno {alumnoMayorPrimerParcial+1} tiene la calificacion más alta: {calificacionMayorPrimerParcial}')
    print(f'En el primer paricial, aprobaron {aprobadosPrimerParcial} alumnos')
    print(f'En el primer paricial, reprobaron {reprobadosPrimerParcial} alumnos\n')

    # Del ultimo parcial, se busca la menor y mayor calificacion, y se cuentan los aprobados y reproados
    alumnoMenorUltimoParcial = 0
    calificacionMenorUltimoParcial = Calificaciones[alumnoMenorUltimoParcial][n-1]
    alumnoMayorUltimoParcial = 0
    calificacionMayorUltimoParcial = Calificaciones[alumnoMayorUltimoParcial][n-1]
    aprobadosUltimoParcial = 0
    reprobadosUltimoParcial = 0

    for i in range(m):

        if Calificaciones[i][n-1] < calificacionMenorUltimoParcial:
            alumnoMenorUltimoParcial = i
            calificacionMenorUltimoParcial = Calificaciones[alumnoMenorUltimoParcial][n-1]

        if Calificaciones[i][n-1] > calificacionMayorUltimoParcial:
            alumnoMayorUltimoParcial = i
            calificacionMayorUltimoParcial = Calificaciones[alumnoMayorUltimoParcial][n-1]

        if Calificaciones[i][n-1] >= 6:
            aprobadosUltimoParcial += 1

        if Calificaciones[i][n-1] < 6:
            reprobadosUltimoParcial += 1

    print(f'En el ultimo paricial, el alumno {alumnoMenorUltimoParcial+1} tiene la calificacion más baja: {calificacionMenorUltimoParcial}')
    print(f'En el ultimo paricial, el alumno {alumnoMayorUltimoParcial+1} tiene la calificacion más alta: {calificacionMayorUltimoParcial}')
    print(f'En el ultimo paricial, aprobaron {aprobadosUltimoParcial} alumnos')
    print(f'En el ultimo paricial, reprobaron {reprobadosUltimoParcial} alumnos\n')
